import pandas as pd
import json
import os

def csv_to_json(file_path):
    # Read the CSV data
    data = pd.read_csv(file_path)
    # Convert to JSON format
    json_data = data.to_dict(orient='records')
    return json_data

def save_json(json_data, output_path):
    with open(output_path, 'w') as f:
        json.dump(json_data, f, indent=4)

# Process multiple CSV files
if __name__ == "__main__":
    files = {
        "Oroville": "./data/Oroville_WML(Sample),.csv",
        "Shasta": "./data/Shasta_WML(Sample),.csv",
        "Sonoma": "./data/Sonoma_WML(Sample),.csv"
    }

    # Loop over each file and convert it to JSON
    for reservoir, csv_path in files.items():
        # Define the output path for the JSON file
        json_output_path = f"./data/{reservoir}_WML,.json"

        # Convert CSV to JSON
        json_data = csv_to_json(csv_path)

        # Save JSON data
        save_json(json_data, json_output_path)
        print(f"Converted {reservoir} CSV to JSON and saved to {json_output_path}")
