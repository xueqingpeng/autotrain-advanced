#!/bin/bash

# federated_learning
# autotrain tools merge-llm-adapter \
#     --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
#     --adapter-path TheFinAI/fl-cleveland-dpo-qlora \
#     --push-to-hub

# autotrain tools merge-llm-adapter \
#     --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
#     --adapter-path TheFinAI/fl-hungarian-dpo-qlora \
#     --push-to-hub

# autotrain tools merge-llm-adapter \
#     --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
#     --adapter-path TheFinAI/fl-switzerland-dpo-qlora \
#     --push-to-hub

# autotrain tools merge-llm-adapter \
#     --base-model-path wendy416/llama32-3b-sft_syn_diabetes \
#     --adapter-path TheFinAI/fl-va-dpo-qlora \
#     --push-to-hub



# fino1
autotrain tools merge-llm-adapter \
    --base-model-path TheFinAI/Fino1-8B \
    --adapter-path TheFinAI/Fino1-8B-dpo-qlora2 \
    --push-to-hub
