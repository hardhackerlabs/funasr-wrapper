#!/bin/bash

source myenv/bin/activate
python transcribe.py --input_file=$1 --output_file=$2 --keywords="$3"