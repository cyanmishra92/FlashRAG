import json
import sys

def convert_format(input_file, output_file):
    # Read the original JSON data
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Prepare and write the converted data to a new JSONL file
    with open(output_file, 'w') as file:
        for index, item in enumerate(data):
            new_entry = {
                "id": f"test_{index}",
                "question": item["Question"],
                "golden_answers": [item["Answer"]]
            }
            # Write each entry as a new line in JSONL format
            file.write(json.dumps(new_entry) + '\n')
    
    print(f"Data successfully converted and saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    convert_format(input_path, output_path)
