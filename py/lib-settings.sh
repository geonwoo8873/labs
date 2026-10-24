#!/usr/bin/env bash

TORCH_VERSION="2.9.1"

if [[ $(python -c "import torch; print(torch.__version__)") > "$TORCH_VERSION" ]]; then
    echo "Torch version is greater than $TORCH_VERSION"
    TORCH_VERSION="2.9.1"
fi

if [[ -r "requirements.txt" ]]; then
    grep -q "torch==$TORCH_VERSION" requirements.txt || echo "torch==$TORCH_VERSION" >> requirements.txt
fi

HUGGINGFACE_HUB_VERSION="2.3.0"

if [[ -r "requirements.txt" ]]; then
    grep -q "huggingface-hub==$HUGGINGFACE_HUB_VERSION" requirements.txt || echo "huggingface-hub==$HUGGINGFACE_HUB_VERSION" >> requirements.txt
fi

TRANSFORMERS_VERSION="5.20.2"

if [[ -r "requirements.txt" ]]; then
    grep -q "transformers==$TRANSFORMERS_VERSION" requirements.txt || echo "transformers==$TRANSFORMERS_VERSION" >> requirements.txt
fi