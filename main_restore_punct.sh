#!/bin/bash

source myenv/bin/activate
python restore_punct.py --input_file=$1 --output_file=$2