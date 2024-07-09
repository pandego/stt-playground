import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
from rich import print as rprint
import os
from typing import Literal
from groq import Groq
from transformers.utils import is_torch_sdpa_available



# --------------------- #
# --- Configuration --- #
# --------------------- #

transcribe: bool = False
translate: bool = False
testing: bool = True

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

rprint(f"SDPA Available: {is_torch_sdpa_available()}")

model_id = "openai/whisper-large-v3"

# ----------------------- #
# --- Load audio file --- #
# ----------------------- #

# filename = os.path.dirname(__file__) + "/sample_audio.m4a"
filename = "recordings/20240709_David_S/20240709_interview_ai_tech_lead_David_S_16000.wav"

# ------------------------------- #
# --- Load model and pipeline --- #
# ------------------------------- #

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, 
    torch_dtype=torch_dtype, 
    low_cpu_mem_usage=True, 
    use_safetensors=True,
    attn_implementation="flash_attention_2",
    # attn_implementation="sdpa",  # If GPU does not support Flash Attention
    )

model.to(device)
rprint(f"Model loaded on '{device.upper()}'! 🚀")

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=25,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

# -------------------------- #
# --- Run model pipeline --- #
# -------------------------- #

if testing:
    dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
    sample = dataset[0]["audio"]

    result = pipe(sample)
    

if transcribe:
    result = pipe(filename, generate_kwargs={"language": "french"})

if translate:
    result = pipe(filename, generate_kwargs={"task": "translate"})

rprint(result["text"])

# -------------------- #
# --- Save Results --- #
# -------------------- #

with open("./result_text.txt", "w") as file:
    file.write(result["text"])
    