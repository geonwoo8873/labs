import logging

import torch


logger = logging.getLogger(__name__)

MODEL_COLLECT = (
    "Qwen/Qwen2.5-0.5B-Instruct",
    "Qwen/Qwen2.5-VL-3B-Instruct",
    "Qwen/Qwen3-4B-Instruct-2507",
    "Qwen/Qwen2.5-Coder-7B-Instruct",
)

CPU_REQUIRED_MODELS = frozenset(
    {
        "Qwen/Qwen2.5-0.5B-Instruct",
        "Qwen/Qwen2.5-VL-3B-Instruct",
        "Qwen/Qwen3-4B-Instruct-2507",
    }
)

CUDA_REQUIRED_MODELS = frozenset({"Qwen/Qwen2.5-Coder-7B-Instruct"})


def resolve_model_config(model_name: str | None = None) -> tuple[str, str]:
    if not MODEL_COLLECT:
        raise ValueError("MODEL_COLLECT must contain at least one model")

    selected_model = MODEL_COLLECT[0] if model_name is None else model_name
    if selected_model not in MODEL_COLLECT:
        raise ValueError(f"Model is not listed in MODEL_COLLECT: {selected_model}")

    if selected_model in CPU_REQUIRED_MODELS:
        return selected_model, "cpu"

    if selected_model in CUDA_REQUIRED_MODELS:
        if not torch.cuda.is_available():
            raise RuntimeError(
                f"{selected_model} requires a CUDA-compatible GPU, but none is available"
            )
        return selected_model, "cuda"

    raise ValueError(f"No device policy is configured for model: {selected_model}")
