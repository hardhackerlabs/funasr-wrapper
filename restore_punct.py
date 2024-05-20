import argparse
import json

from funasr import AutoModel

def process_sentence(model, long):
    print(f"Processing sentence: {long}")
    res = model.generate(input=long)
    if len(res) > 0:
        text = res[0]["text"]
    else:
        text = long
    return text

def main():
    parser = argparse.ArgumentParser(description='Restore punctuation.')
    parser.add_argument('--input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('--output_file', type=str, help='Path to the output JSON file')
    args = parser.parse_args()
    
    with open(args.input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("The input JSON file must contain a list.")
    
    model = AutoModel(model="ct-punc", device="cpu", ncpu=4)
    results = []
    for text in data:
        text = process_sentence(model, text)
        results.append(text)
    
    # Save the results to the output file
    with open(args.output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
