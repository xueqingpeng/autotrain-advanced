#!/bin/bash

source .env
echo "HF_USERNAME: $HF_USERNAME"
echo "HF_TOKEN: $HF_TOKEN" | cut -c1-20

export VLLM_WORKER_MULTIPROC_METHOD="spawn"
export CUDA_VISIBLE_DEVICES=0,1

# python federated_learning/dpo/data_convert.py

# autotrain --config federated_learning/dpo/fl-cleveland-dpo-qlora.yml
# autotrain --config federated_learning/dpo/fl-hungarian-dpo-qlora.yml
# autotrain --config federated_learning/dpo/fl-switzerland-dpo-qlora.yml
# autotrain --config federated_learning/dpo/fl-va-dpo-qlora.yml

# bash merge.sh

# autotrain --config federated_learning/sft/fl-cleveland-sft.yml
# autotrain --config federated_learning/sft/fl-hungarian-sft.yml
# autotrain --config federated_learning/sft/fl-switzerland-sft.yml
# autotrain --config federated_learning/sft/fl-va-sft.yml

autotrain --config fino1/dpo/Fino1-8B-dpo-qlora2.yml
bash merge.sh
