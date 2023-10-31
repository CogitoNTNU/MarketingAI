import csv
import json
import os

# Directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Finding the first .csv file in the directory
csv_filename = next((f for f in os.listdir(script_dir) if f.endswith('.csv')), None)

if csv_filename:
    csv_filepath = os.path.join(script_dir, csv_filename)
    jsonl_filename = "MarketingFinetuning.jsonl"
    
    # Define the field names based on the structure of your CSV
    fieldnames = ["prompt", "response"]
    
    # Open the CSV file for reading and the JSONL file for writing
    with open(csv_filepath, 'r', encoding='utf-8') as csv_file, open(jsonl_filename, 'w', encoding='utf-8') as jsonl_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        
        # Skip the header (if it exists)
        next(csv_reader, None)
        
        # Iterate over CSV rows
        for row in csv_reader:
            # Create the desired JSON object format
            json_obj = {
                "messages": [
                    {
                        "role": "system",
                        "content": "Marv is a factual chatbot that is also sarcastic."
                    },
                    {
                        "role": "user",
                        "content": row["prompt"].strip()
                    },
                    {
                        "role": "assistant",
                        "content": row["response"].strip()
                    }
                ]
            }
            
            # Write the JSON object to the JSONL file
            jsonl_file.write(json.dumps(json_obj) + '\n')
            
    print(f"JSONL file has been created from {csv_filename}")
else:
    print("No CSV file found in the script directory.")
