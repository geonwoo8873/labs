import logging
import threading
import time
from typing import Any

import fastapi
import torch

import model as model_config


app = fastapi.FastAPI()
logger = logging.getLogger(__name__)

_llm_model = None
_llm_tokenizer = None
_llm_load_seconds = None
_llm_device = None
_model_load_lock = threading.Lock()


def _load_model() -> tuple[Any, Any, float, str]:
    global _llm_model, _llm_tokenizer, _llm_load_seconds, _llm_device

    if (
        _llm_model is not None
        and _llm_tokenizer is not None
        and _llm_load_seconds is not None
        and _llm_device is not None
    ):
        return _llm_model, _llm_tokenizer, _llm_load_seconds, _llm_device

    with _model_load_lock:
        if (
            _llm_model is not None
            and _llm_tokenizer is not None
            and _llm_load_seconds is not None
            and _llm_device is not None
        ):
            return _llm_model, _llm_tokenizer, _llm_load_seconds, _llm_device

        from transformers import AutoModelForCausalLM, AutoTokenizer

        model_name, device = model_config.resolve_model_config()
        logger.info("Loading %s on %s", model_name, device)
        load_started_at = time.perf_counter()
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        ).to(device)
        model.eval()
        if device == "cuda":
            torch.cuda.synchronize()

        _llm_tokenizer = tokenizer
        _llm_model = model
        _llm_device = device
        _llm_load_seconds = time.perf_counter() - load_started_at
        return model, tokenizer, _llm_load_seconds, device


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/generate")
def generate(
    prompt: str = fastapi.Query(min_length=1),
    max_new_tokens: int = fastapi.Query(default=128, ge=1, le=2048),
):
    llm_model, tokenizer, load_seconds, device = _load_model()

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    if device == "cuda":
        torch.cuda.synchronize()
    generation_started_at = time.perf_counter()
    with torch.inference_mode():
        output = llm_model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )
    if device == "cuda":
        torch.cuda.synchronize()
    generation_seconds = time.perf_counter() - generation_started_at

    generated_tokens = output[0, inputs["input_ids"].shape[1] :]
    generated_token_count = generated_tokens.shape[0]
    return {
        "response": tokenizer.decode(generated_tokens, skip_special_tokens=True),
        "model_load_seconds": round(load_seconds, 3),
        "generation_seconds": round(generation_seconds, 3),
        "generated_tokens": generated_token_count,
        "tokens_per_second": round(generated_token_count / generation_seconds, 2)
        if generation_seconds > 0
        else 0,
    }
