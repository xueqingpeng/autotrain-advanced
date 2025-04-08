#!/bin/bash

autotrain tools merge-llm-adapter \
    --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
    --adapter-path TheFinAI/fl-cleveland-dpo-qlora \
    --push-to-hub

autotrain tools merge-llm-adapter \
    --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
    --adapter-path TheFinAI/fl-hungarian-dpo-qlora \
    --push-to-hub

autotrain tools merge-llm-adapter \
    --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
    --adapter-path TheFinAI/fl-switzerland-dpo-qlora \
    --push-to-hub

autotrain tools merge-llm-adapter \
    --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
    --adapter-path TheFinAI/fl-va-dpo-qlora \
    --push-to-hub