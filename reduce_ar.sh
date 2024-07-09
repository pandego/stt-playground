#!/bin/bash

# Reduce the file size of an audio file by changing the audio sample rate

input_file="$1"
ar="$2"
output_file="${input_file%.*}_${ar}.${input_file##*.}"

ffmpeg \
    -i "$input_file" \
    -ar "$ar" \
    -ac 1 \
    -map 0:a: \
    "$output_file"
