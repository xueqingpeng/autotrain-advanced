from datasets import load_dataset, Dataset
import pandas as pd
import json


df_hf_paths = [
    # "SahmBenchmark/financial-reports-extractive-summarization_train",
    # "SahmBenchmark/Islamic_Finance_QnA_train",
    # "SahmBenchmark/arabic-financial-qa_train",
    # "SahmBenchmark/fatwa-training_standardized",

    # "SahmBenchmark/arabic-accounting-mcq_train",
    # "SahmBenchmark/arabic-business-mcq_training_standardized",
    # "SahmBenchmark/Sentiment_Analysis_MCQ_train",

    "SahmBenchmark/arabic-accounting-mcq_conversational",
    "SahmBenchmark/sentiment-analysis-mcq_conversational",
    "SahmBenchmark/arabic-business-mcq_conversational",
]


# output_df = []
for df_hf_path in df_hf_paths:
    # load the data from huggingface
    dataset = load_dataset(df_hf_path)

    train = dataset["train"]
    df_train = pd.DataFrame(train)
    print(f"* loaded {len(df_train)} rows from {df_hf_path}")
    # # take an overview of the train data
    # print(df_train.head())
    # print([i["role"] for i in df_train["conversations"][0]])

    for i, r in df_train.iterrows():
        conversations = r["conversations"]
        for conversation in conversations:
            conversation['role'] = 'user' if conversation['role'] == 'human' else 'assistant'
        df_train.at[i, 'conversations'] = conversations

    # push the data to huggingface
    hf_dataset = Dataset.from_pandas(df_train[["id", "conversations"]])
    hf_dataset.push_to_hub(f"{df_hf_path}_formatted")

    # output_df.append(df_train[["id", "conversations"]])

# output_df = pd.concat(output_df)
# print(f"* total {len(output_df)} rows")
# print(output_df.head())

# # push the data to huggingface
# hf_dataset = Dataset.from_pandas(output_df)
# hf_dataset.push_to_hub("SahmBenchmark/train_tg")





df_hf_paths = [
    "SahmBenchmark/arabic-accounting-mcq_conversational_formatted",
    "SahmBenchmark/arabic-business-mcq_conversational_formatted", 
    "SahmBenchmark/arabic-financial-qa_train_formatted",
    "SahmBenchmark/Islamic_Finance_QnA_train_formatted",
    "SahmBenchmark/financial-reports-extractive-summarization_train_formatted",
]

# 合并数据集
merged_data = []
for path in df_hf_paths:
    dataset = load_dataset(path)["train"]
    merged_data.append(pd.DataFrame(dataset))
    print(f"Loaded {len(dataset)} rows from {path}")

# 上传到HF
combined_df = pd.concat(merged_data, ignore_index=True)
print(f"Total: {len(combined_df)} rows")

hf_dataset = Dataset.from_pandas(combined_df)
hf_dataset.push_to_hub("SahmBenchmark/arabic-financial-merged-sft")
print("✅ Uploaded to HF")

