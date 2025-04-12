#!/bin/bash

source .env
echo "HF_USERNAME: $HF_USERNAME"
echo "HF_TOKEN: $HF_TOKEN" | cut -c1-20

export VLLM_WORKER_MULTIPROC_METHOD="spawn"
export CUDA_VISIBLE_DEVICES=4,5,6,7

# python dpo/data_convert.py

# autotrain --config dpo/fl-cleveland-dpo-qlora.yml
# autotrain --config dpo/fl-hungarian-dpo-qlora.yml
# autotrain --config dpo/fl-switzerland-dpo-qlora.yml
# autotrain --config dpo/fl-va-dpo-qlora.yml

# bash merge.sh

autotrain --config sft/fl-cleveland-sft.yml
autotrain --config sft/fl-hungarian-sft.yml
autotrain --config sft/fl-switzerland-sft.yml
autotrain --config sft/fl-va-sft.yml