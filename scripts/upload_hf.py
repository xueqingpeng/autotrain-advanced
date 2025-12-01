#!/usr/bin/env python3
"""
简化的模型上传脚本
"""

import os
from huggingface_hub import HfApi

# 配置
MODEL_PATH = "/gpfs/radev/home/xp83/Documents/project/scripts/autotrain-advanced/scripts/arabic-merged-sft"
REPO_ID = "SahmBenchmark/arabic-merged-sft"

def main():
    print(f"上传模型: {MODEL_PATH}")
    print(f"目标仓库: {REPO_ID}")
    
    try:
        api = HfApi()
        
        # 创建仓库
        api.create_repo(repo_id=REPO_ID, exist_ok=True, private=False)
        print("✓ 仓库创建完成")
        
        # 上传整个文件夹
        api.upload_folder(
            folder_path=MODEL_PATH,
            repo_id=REPO_ID,
            ignore_patterns=["runs/"]  # 忽略训练日志
        )
        
        print(f"✅ 上传成功!")
        print(f"🔗 查看模型: https://huggingface.co/{REPO_ID}")
        
    except Exception as e:
        print(f"❌ 上传失败: {e}")

if __name__ == "__main__":
    main()
