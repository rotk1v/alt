import os
import subprocess
import json

script_folder = "./scrapers"
results_folder = "./results"

script_args = [results_folder]

for filename in os.listdir(script_folder):
    if filename.endswith(".py"):
        script_path = os.path.join(script_folder, filename)
        subprocess.run(["python", script_path] + script_args)


output_file = "results-all.json"
combined_data = []
for filename in os.listdir(results_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(results_folder, filename)
        with open(filepath, "r") as f:
            combined_data.extend(json.load(f))

with open(os.path.join(results_folder, output_file), "w") as f:
    json.dump(combined_data, f, indent=4)
