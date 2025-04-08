from datasets import load_dataset
import pandas as pd
import json
import os
from huggingface_hub import create_repo
from huggingface_hub import upload_file


def data_load(fp):
    data = []
    with open(fp, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    df = pd.DataFrame(data)
    return df


def add_prompt(df):
    prompts = []
    # for i, r in enumerate(df):
    for i, r in df.iterrows():
        chosen = r["chosen"]
        prompt = ""
        # 拼接除了最后一句之外的对话内容
        for chosen_i in chosen[:len(chosen)-1]:
            content = chosen_i["content"]
            role = chosen_i["role"]
            prompt += f"<|{role}|>\n{content}</s>\n"
        prompts.append(prompt)
        # print(json.dumps(prompt, ensure_ascii=False))

    df["prompt"] = prompts
    return df


def data_convert(fp_in, fp_out):
    df = data_load(fp_in)
    df = add_prompt(df)
    df.to_json(fp_out, orient="records", lines=True, force_ascii=False)
    return df


dir = "/home/xpeng3/SynFed/syned_datasets/syn1_dpo"
for df_name in ["cleveland", "hungarian", "switzerland", "va"]:
    # data convert
    fp_in = os.path.join(dir, f"{df_name}/{df_name}.pref.jsonl")
    fp_out = os.path.join(dir, f"{df_name}.jsonl")
    df = data_convert(fp_in, fp_out)

    # upload to huggingface
    repo_id = f"TheFinAI/syn1_dpo_{df_name}"

    print(f"* creating or overwriting {repo_id}!")
    create_repo(repo_id, repo_type="dataset", exist_ok=True)

    print(f"* uploading to {repo_id}!")
    upload_file(
        path_or_fileobj=fp_out,
        path_in_repo="train.jsonl",
        repo_id=repo_id,
        repo_type="dataset"
    )










# # Load the dataset
# dataset = load_dataset("argilla/distilabel-capybara-dpo-7k-binarized")
# train_data = dataset["train"]

# # See a sample
# print("*** prompt ***")
# print(json.dumps(train_data["prompt"][0], ensure_ascii=False))
# # # print("*** chosen ***")
# # # print(json.dumps(train_data["chosen"][0], ensure_ascii=False))
# # # print("*** rejected ***")
# # # print(json.dumps(train_data["rejected"][0], ensure_ascii=False))

# # Check available columns
# print(train_data.column_names)
# df = add_prompt(train_data)