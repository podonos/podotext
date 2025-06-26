"""
Text-to-Speech Generation Script using Mello TTS

- Model: Mello TTS (via melo.api)
- GitHub Repository: https://github.com/myshell-ai/MeloTTS 
- Language: English ('EN'), using 'EN-US' speaker
- Requirements:
    - melo
    - pandas
    - tqdm
    - PyTorch
    - CUDA-compatible GPU (optional; CPU works too)

"""

# Import necessary libraries
from melo.api import TTS           
import pandas as pd                
from tqdm import tqdm              
import os

# Set speech speed (1.0 = normal speed)
speed = 1.0

# Device selection: 'auto' selects GPU if available, otherwise CPU
device = 'auto'

# Initialize the Mello TTS model with English language setting
model = TTS(language='EN', device=device)

# Get speaker ID mapping from model
speaker_ids = model.hps.data.spk2id

# Load the sentence list from CSV (⚠️ note: typo in filename extension below)
df_concat = pd.read_csv("")  # ← Might be typo: should be .csv

# Iterate over all rows in the DataFrame
for i in tqdm(range(df_concat.shape[0])):
    try:
        # Get sentence text from the first column
        temp_text = df_concat.iloc[i, 0]

        # Define the path to save the output .wav file
        output_path = ''

        # Generate speech and save to file using EN-US speaker
        model.tts_to_file(temp_text, speaker_ids['EN-US'], output_path, speed=speed)

    except Exception as e:
        # Print the error details if generation fails
        print(f"[❌ Error at index {i}] Text: {temp_text}")
        print(f"    → Error: {e}")
