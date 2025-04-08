#!/bin/bash

source .env
echo "HF_USERNAME: $HF_USERNAME"
echo "HF_TOKEN: $HF_TOKEN" | cut -c1-20

autotrain --config fl-cleveland-sft.yml
autotrain --config fl-hungarian-sft.yml
autotrain --config fl-switzerland-sft.yml
autotrain --config fl-va-sft.yml