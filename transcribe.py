import argparse
import json

from funasr import AutoModel

def main():
    parser = argparse.ArgumentParser(description='Transcribe audio file.')
    parser.add_argument('--input_file', type=str, help='Path to the input audio file')
    parser.add_argument('--output_file', type=str, help='Path to the output JSON file')
    parser.add_argument('--keywords', type=str, help='Keywords as hotword')
    args = parser.parse_args()

    model = AutoModel(model="paraformer-zh",
                        vad_model="fsmn-vad",
                        punc_model="ct-punc",
                        device="cuda:0",
                        ncpu=4,
                        spk_model="cam++", 
                     )
    results = model.generate(input=args.input_file, 
                        batch_size_s=300,
                        batch_size_threshold_s=60,
                        hotword=args.keywords,
                        )
    if len(results) > 0:
        sentences = results[0]["sentence_info"]
        segments = []
        for sentence in sentences:
            spk = sentence['spk'] + 1
            new_segment = {
                "start": sentence["start"],
                "end": sentence["end"],
                "speaker": "Speaker " + str(spk),
                "text": sentence["text"],
                "language": "zh"
            }
            segments.append(new_segment)
        # Save the segments to the output file
        with open(args.output_file, 'w', encoding='utf-8') as file:
            json.dump(segments, file, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    main()