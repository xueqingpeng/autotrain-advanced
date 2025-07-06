#!/bin/bash

source .env
echo "HF_USERNAME: $HF_USERNAME"
echo "HF_TOKEN: $HF_TOKEN" | cut -c1-20
echo "WANDB_ENTITY: $WANDB_ENTITY"
echo "WANDB_API_KEY: $WANDB_API_KEY" | cut -c1-20

export VLLM_WORKER_MULTIPROC_METHOD="spawn"
export CUDA_VISIBLE_DEVICES=0,1

# python federated_learning/dpo/data_convert.py
# autotrain --config federated_learning/dpo/fl-cleveland-dpo-qlora.yml
# autotrain --config federated_learning/dpo/fl-hungarian-dpo-qlora.yml
# autotrain --config federated_learning/dpo/fl-switzerland-dpo-qlora.yml
# bash merge.sh

# autotrain --config federated_learning/sft/fl-cleveland-sft.yml
# autotrain --config federated_learning/sft/fl-hungarian-sft.yml
# autotrain --config federated_learning/sft/fl-switzerland-sft.yml
# autotrain --config federated_learning/sft/fl-va-sft.yml
# bash merge.sh

# autotrain --config federated_learning/sft/testing/fl-cleveland-sft-top.yml
# autotrain --config federated_learning/sft/testing/fl-hungarian-sft-top.yml
# autotrain --config federated_learning/sft/testing/fl-switzerland-sft-top.yml

# autotrain --config federated_learning/sft/testing/fl-cleveland-sft-bottom.yml
# autotrain --config federated_learning/sft/testing/fl-hungarian-sft-bottom.yml
# autotrain --config federated_learning/sft/testing/fl-switzerland-sft-bottom.yml

# autotrain --config federated_learning/sft/testing/fl-cleveland-sft-pos.yml
# autotrain --config federated_learning/sft/testing/fl-hungarian-sft-pos.yml
# autotrain --config federated_learning/sft/testing/fl-switzerland-sft-pos.yml

# autotrain --config federated_learning/sft/testing/fl-cleveland-sft-neg.yml
# autotrain --config federated_learning/sft/testing/fl-hungarian-sft-neg.yml
# autotrain --config federated_learning/sft/testing/fl-switzerland-sft-neg.yml

# autotrain --config fino1/dpo/Fino1-8B-dpo-qlora2.yml
# bash merge.sh
