#!/bin/bash

source .env
echo "HF_USERNAME: $HF_USERNAME"
echo "HF_TOKEN: $HF_TOKEN" | cut -c1-20

autotrain --config fl-cleveland-dpo-qlora.yml
autotrain --config fl-hungarian-dpo-qlora.yml
autotrain --config fl-switzerland-dpo-qlora.yml
autotrain --config fl-va-dpo-qlora.yml