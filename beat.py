from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import os
import torch
import scipy.io.wavfile as wavfile


load_dotenv(find_dotenv())



def instrumental_generation(prompt):
    text_to_beats= pipeline("text-to-audio", "facebook/musicgen-small")
    beats= text_to_beats(prompt, forward_params={"do_sample": True})
    wavfile.write("beat.wav", rate=beats["sampling_rate"], data=beats["audio"])
    return "beat.wav"

# prompt_rap= "West Coast style hip hop beat with heavy 808 and drums"

# music_generation(prompt_rap)