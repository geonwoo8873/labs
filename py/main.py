import torch
import fastapi

app = fastapi.FastAPI()

print("torch:", torch.__version__)
print("hip:", torch.version.hip)
print("cuda.is_available:", torch.cuda.is_available())

try:
    x = torch.tensor([1.0, 2.0, 3.0], device="cuda")
    y = x * 2
    print("GPU tensor ok:", y, y.device)
except Exception as e:
    print("GPU tensor failed:", repr(e))

import time


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

_llm_model = None
_llm_tokenizer = None
_llm_load_seconds = None
_llm_device = "cuda" if torch.cuda.is_available() else "cpu"

# Qwen/Qwen2.5-VL-3B-Instruct : VRAM 8GB -2
# "model_load_seconds":124.486,"generation_seconds":3.638,"generated_tokens":128,"tokens_per_second":19.19 OK
# "model_load_seconds":5.842,"generation_seconds":3.632,"generated_tokens":128,"tokens_per_second":35.24 OK
# "model_load_seconds":5.475,"generation_seconds":3.659,"generated_tokens":128,"tokens_per_second":34.98 OK
# Qwen/Qwen3-4B-Instruct-2507 : VRAM 8GB -2
# "model_load_seconds":9.609,"generation_seconds":5.121,"generated_tokens":128,"tokens_per_second":25.0 Ok
# "model_load_seconds":6.984,"generation_seconds":3.976,"generated_tokens":128,"tokens_per_second":32.2 Ok
# "model_load_seconds":7.038,"generation_seconds":3.861,"generated_tokens":128,"tokens_per_second":33.15 Ok
# Qwen/Qwen2.5-Coder-7B-Instruct : VRAM 15GB -2
# "model_load_seconds":18.263,"generation_seconds":9.79,"generated_tokens":128,"tokens_per_second":13.07 OK3
# "model_load_seconds":17.988,"generation_seconds":9.884,"generated_tokens":128,"tokens_per_second":12.95 OK
# "model_load_seconds":17.988,"generation_seconds":8.588,"generated_tokens":128,"tokens_per_second":14.9 OK

## Remove this section if not needed for other models : hf cache rm <model_name>

@app.get("/generate")
def generate(
    prompt: str = fastapi.Query(min_length=1),
    max_new_tokens: int = fastapi.Query(default=128, ge=1, le=2048),
):
    global _llm_model, _llm_tokenizer, _llm_load_seconds

    if _llm_model is None or _llm_tokenizer is None:
        from transformers import AutoModelForCausalLM, AutoTokenizer

        load_started_at = time.perf_counter()
        model_name = "Qwen/Qwen2.5-VL-3B-Instruct"
        _llm_tokenizer = AutoTokenizer.from_pretrained(model_name)
        _llm_model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
        ).to(_llm_device)
        _llm_model.eval()
        if _llm_device == "cuda":
            torch.cuda.synchronize()
        _llm_load_seconds = time.perf_counter() - load_started_at

    inputs = _llm_tokenizer(prompt, return_tensors="pt").to(_llm_device)
    if _llm_device == "cuda":
        torch.cuda.synchronize()
    generation_started_at = time.perf_counter()
    with torch.inference_mode():
        output = _llm_model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )
    if _llm_device == "cuda":
        torch.cuda.synchronize()
    generation_seconds = time.perf_counter() - generation_started_at

    generated_tokens = output[0, inputs["input_ids"].shape[1]:]
    generated_token_count = generated_tokens.shape[0]
    return {
        "response": _llm_tokenizer.decode(generated_tokens, skip_special_tokens=True),
        "model_load_seconds": round(_llm_load_seconds, 3),
        "generation_seconds": round(generation_seconds, 3),
        "generated_tokens": generated_token_count,
        "tokens_per_second": round(generated_token_count / generation_seconds, 2)
        if generation_seconds > 0
        else 0,
    }
