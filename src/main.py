# 🚀 Step 2: Import Libraries
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
import json

# 🚀 Step 3: Load Model and Tokenizer
model_id = "Qwen/Qwen1.5-0.5B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 🚀 Step 4: Load Prompt Templates from prompts/*.txt
prompt_dir = "/content/Prompt-Engineering-Lab/Prompt-Engineering-Lab/prompts"
prompt_types = ["zero_shot", "few_shot", "cot_prompt", "meta_prompt"]
prompt_templates = {}

for pt in prompt_types:
    file_path = os.path.join(prompt_dir, f"{pt}.txt")
    with open(file_path, "r") as f:
        prompt_templates[pt] = f.read().strip()

# 🚀 Step 5: Load Queries from evaluation/input_queries.json
with open("/content/Prompt-Engineering-Lab/Prompt-Engineering-Lab/evaluation/input_queries.json", "r") as f:
    queries = json.load(f)

# 🚀 Step 6: Define the Response Generator
def generate_response(prompt, max_tokens=256):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("A:")[-1].strip()

# 🚀 Step 7: Run All Prompt Types for All Queries
output_logs = {pt: [] for pt in prompt_types}

print("🚀 Starting evaluations...\n")
for i, query in enumerate(queries):
    print(f"🔍 Query {i+1}/{len(queries)}: {query}")

    for pt in prompt_types:
        full_prompt = f"{prompt_templates[pt]}\nQ: {query}\nA:"
        print(f"   ⏳ Running {pt.replace('_', ' ').title()}...")
        response = generate_response(full_prompt)
        output_logs[pt].append({
            "query": query,
            "response": response
        })
        print(f"   ✅ {pt.replace('_', ' ').title()} complete.")

# 🚀 Step 8: Save Results
os.makedirs("/content/Prompt-Engineering-Lab/Prompt-Engineering-Lab/evaluation", exist_ok=True)
with open("/content/Prompt-Engineering-Lab/Prompt-Engineering-Lab/evaluation/output_logs.json", "w") as f:
    json.dump(output_logs, f, indent=2)

print("\n✅ All outputs saved to evaluation/output_logs.json.")
