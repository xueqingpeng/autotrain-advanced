from datasets import load_dataset
import pandas as pd
import json

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

# fp_in = "/home/xp83/Documents/project/data/syn1_dpo/cleveland/cleveland.pref.jsonl"
# fp_out = "/home/xp83/Documents/project/data/syn1_dpo/cleveland.jsonl"
# data_convert(fp_in, fp_out)
# fp_in = "/home/xp83/Documents/project/data/syn1_dpo/hungarian/hungarian.pref.jsonl"
# fp_out = "/home/xp83/Documents/project/data/syn1_dpo/hungarian.jsonl"
# data_convert(fp_in, fp_out)
# fp_in = "/home/xp83/Documents/project/data/syn1_dpo/switzerland/switzerland.pref.jsonl"
# fp_out = "/home/xp83/Documents/project/data/syn1_dpo/switzerland.jsonl"
# data_convert(fp_in, fp_out)
# fp_in = "/home/xp83/Documents/project/data/syn1_dpo/va/va.pref.jsonl"
# fp_out = "/home/xp83/Documents/project/data/syn1_dpo/va.jsonl"
# data_convert(fp_in, fp_out)



# List your input and output JSONL files
input_files = [
    '/home/xp83/Documents/project/data/syn1_dpo/cleveland.jsonl', 
    '/home/xp83/Documents/project/data/syn1_dpo/hungarian.jsonl', 
    '/home/xp83/Documents/project/data/syn1_dpo/switzerland.jsonl', 
    '/home/xp83/Documents/project/data/syn1_dpo/va.jsonl'
]
output_file = '/home/xp83/Documents/project/data/syn1_dpo/combined.jsonl'

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    for file in input_files:
        with open(file, 'r', encoding='utf-8') as infile:
            for line in infile:
                # Ensure each line is stripped and re-dumped as JSON for formatting consistency
                data = json.loads(line)
                json.dump(data, outfile)
                outfile.write('\n')

print(f"Combined {len(input_files)} files into '{output_file}'")





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