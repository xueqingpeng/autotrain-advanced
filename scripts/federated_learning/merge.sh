#!/bin/bash

source .env
echo "HF_USERNAME: $HF_USERNAME"
echo "HF_TOKEN: $HF_TOKEN" | cut -c1-20

autotrain tools merge-llm-adapter \
    --base-model-path Qwen/Qwen2.5-3B \
    --adapter-path TheFinAI/fl-cleveland-dpo-qlora \
    --push-to-hub

autotrain tools merge-llm-adapter \
    --base-model-path Qwen/Qwen2.5-3B \
    --adapter-path TheFinAI/fl-hungarian-dpo-qlora \
    --push-to-hub

autotrain tools merge-llm-adapter \
    --base-model-path Qwen/Qwen2.5-3B \
    --adapter-path TheFinAI/fl-switzerland-dpo-qlora \
    --push-to-hub

autotrain tools merge-llm-adapter \
    --base-model-path Qwen/Qwen2.5-3B \
    --adapter-path TheFinAI/fl-va-dpo-qlora \
    --push-to-hub