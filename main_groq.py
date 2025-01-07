import os
from typing import Literal
from groq import Groq


# --------------------- #
# --- Configuration --- #
# --------------------- #

transcribe: bool = True
translate: bool = False

client = Groq()

model: str = "whisper-large-v3"
response_format: Literal[
  'json', 'text', 'verbose_json'] = 'text'
temperature=0.0

# ----------------------- #
# --- Load audio file --- #
# ----------------------- #

filename = os.path.dirname(__file__) + "/sample_audio.m4a"

# ------------------------------------ #
# --- Translate audio file to text --- #
# ------------------------------------ #

if transcribe:
  
  """
  Optional Parameters:

    - prompt: Provide context or specify how to spell unfamiliar words
    - response_format: Define the output response format.
      - Default is "json"
      - Set to "verbose_json" to receive timestamps for audio segments
      - Set to "text" to return a text response
      - formats vtt and srt are not supported
    - temperature: Specify a value between 0 and 1 to control the translation output.
    - language: Specify the language for transcription (optional; Whisper will auto-detect if not specified)
      - Use ISO 639-1 language codes (e.g., "en" for English, "fr" for French, etc.).
      - Specifying a language may improve transcription accuracy and speed
    - timestamp_granularities[] is not supported
  """
  
  prompt: str = "Specify context or spelling"
  language: str = 'fr'           # "en" for English, "fr" for French, etc

  with open(filename, "rb") as file:
      transcription  = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model=model,
        # prompt=prompt,                  # Optional
        response_format=response_format,  # Optional
        language=language,                # Optional
        temperature=0.0,                  # Optional
      )
      print(transcription.text)
      result = transcription.text


# --------------------------------------- #
# --- Translate audio file to English --- #
# --------------------------------------- #

if translate:
  
  """
  Optional Parameters:

    - prompt: Provide context or specify how to spell unfamiliar words
    - response_format: Define the output response format:
      - Default is "json"
      - Set to "verbose_json" to receive timestamps for audio segments
      - Set to "text" to return a text response
      - formats vtt and srt are not supported
    - temperature: Specify a value between 0 and 1 to control the translation output
  """
  
  prompt: str = "Specify context or spelling"

  with open(filename, "rb") as file:
      translation = client.audio.translations.create(
        file=(filename, file.read()),
        model=model,
        prompt=prompt,                    # Optional
        response_format=response_format,  # Optional
        temperature=0.0,                  # Optional
        )
      print(translation.text)
      result = translation.text
      

# -------------------- #
# --- Save Results --- #
# -------------------- #

with open("./result_text.txt", "w") as file:
    file.write(result)
