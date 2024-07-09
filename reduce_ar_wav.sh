#!/bin/bash

# Convert an m4a audio file to wav format and reduce the sample rate

input_file="$1"
ar="$2"
output_file="${input_file%.*}_${ar}.wav"

ffmpeg \
    -i "$input_file" \
    -ar "$ar" \
    -ac 1 \
    "$output_file"
