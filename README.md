# STT Playground
## Intro
A playground for STT using API calls and local models.

## Pre-requisits
- Conda
- GPU (Nvidia)

# Environment
This was testing on **Ubuntu only**, but it should work well on **MacOS** and **Windows WSL**.
- Clone this repo:
    ```bash
    git clone https://github.com/pandego/stt-playground.git
    cd sst-playground
    ```

- Setup the environment:
    ```bash
    conda env create -f environment.yml
    conda activate whisper
    ```

- Install dependencies:
    ```bash
    poetry install --no-root
    poetry run pip install flash-attn --no-build-isolation
    ```

# Test it out
If all went well with the environment setup, you should be able to test it pretty quickly.

## Local
- Run the following command to convert any `m4a` file to wav and reduce the AR.
    ```bash
    sh reduce_ar_wav.sh recordings/sample.m4a 8000
    ```
- Run main script:
    ```bash
    python main_local.py
    ```
- A `result_text.txt` should appear in the work-directory.

## Using GroQ API
- Run the following command to take any `m4a` file and reduce the AR.
    ```bash
    sh reduce_ar.sh recordings/sample.m4a 8000
    ```
- Run main script:
    ```bash
    python main_groq.py
    ```
- A `result_text.txt` should appear in the work-directory.

_Et Voilà !_ 🎈