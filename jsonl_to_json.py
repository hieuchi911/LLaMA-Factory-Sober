import json

# Step 1: Open the .jsonl file for reading
BASE_PATH="/home/zihaoh/repos/i-am-sober/processed_data/cnn_dailymail/full-1024-512/llama/"

for split in ["train", "valid"]:
    input_file_path = BASE_PATH + split + ".jsonl"
    output_file_path = BASE_PATH + split + ".json"

    # Initialize an empty list to hold the JSON objects
    json_objects = []

    with open(input_file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            json_object = json.loads(line)
            json_objects.append(json_object)

    with open(output_file_path, 'w') as json_file:
        json.dump(json_objects, json_file, indent=4)