import json
import sys
import random

def sample_questions(input_file, output_file, n):
    # Read the JSON Lines from the input file
    with open(input_file, 'r') as file:
        data = [json.loads(line.strip()) for line in file]

    # Check if the requested sample size is greater than available data
    if n > len(data):
        print("Requested number of questions exceeds the number of available entries.")
        sys.exit(1)

    # Randomly sample n questions
    sampled_data = random.sample(data, n)

    # Update the 'id' field to be sequential from 0 to n-1
    for index, item in enumerate(sampled_data):
        item['id'] = f"test_{index}"

    # Write the sampled data to a new JSONL file
    with open(output_file, 'w') as file:
        for item in sampled_data:
            file.write(json.dumps(item) + '\n')

    print(f"Randomly selected data successfully saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file_path> <output_file_path> <number_of_questions>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    number_of_questions = int(sys.argv[3])
    
    sample_questions(input_path, output_path, number_of_questions)
