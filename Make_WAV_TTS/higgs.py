from boson_multimodal.serve.serve_engine import HiggsAudioServeEngine, HiggsAudioResponse
from boson_multimodal.data_types import ChatMLSample, Message, AudioContent

import torch
import torchaudio
import time
import click

import pandas as pd

import sys
sys.setrecursionlimit(3000)

MODEL_PATH = "bosonai/higgs-audio-v2-generation-3B-base"
AUDIO_TOKENIZER_PATH = "bosonai/higgs-audio-v2-tokenizer"

device = "cuda" if torch.cuda.is_available() else "cpu"

serve_engine = HiggsAudioServeEngine(MODEL_PATH, AUDIO_TOKENIZER_PATH, device=device)

df_concat = pd.read_csv("") # dataset url

device = "cuda" if torch.cuda.is_available() else "cpu"
system_prompt = (
    "Generate audio following instruction.\n\n<|scene_desc_start|>\nAudio is recorded from a quiet room.\n<|scene_desc_end|>" # system prompt for higgs
)
from tqdm import tqdm

# generate wav file using text script

for i in tqdm(range(df_concat.shape[0])):
    
    try:
        temp_text = df_concat.iloc[i,2]
        messages = [
        Message(
            role="system",
            content=system_prompt,
        ),
        Message(
            role="user",
            content=temp_text,
            ),
        ]
        
        output: HiggsAudioResponse = serve_engine.generate(
            chat_ml_sample=ChatMLSample(messages=messages),
            max_new_tokens=1024,
            temperature=0.5,
            top_p=0.95,
            top_k=50,
            stop_strings=["<|end_of_text|>", "<|eot_id|>"],
        )
        
        
        torchaudio.save(f".wav", torch.from_numpy(output.audio)[None, :], output.sampling_rate) # save wav file

    except Exception as e:
        print(f"[❌ Error at index {i}] Text: {temp_text}")
        print(f"    → Error: {e}")
