"""
Text-to-Speech Generation Script using Chatterbox TTS

- Model: Chatterbox TTS
- GitHub Repository: https://github.com/resemble-ai/chatterbox
- Requirements:
    - chatterbox (install from GitHub)
    - torchaudio
    - pandas
    - tqdm
    - CUDA-enabled GPU for inference

"""

# Import necessary libraries
import torchaudio as ta                           
from chatterbox.tts import ChatterboxTTS          
import pandas as pd                               
import os
import sys
from tqdm import tqdm  


# Increase the recursion limit (if necessary for model internals)
sys.setrecursionlimit(3000)

# Load the pre-trained Chatterbox TTS model onto GPU
model = ChatterboxTTS.from_pretrained(device="cuda")

# Load the CSV file containing text data
df_concat = pd.read_csv("")

# Iterate through each row in the DataFrame
for i in tqdm(range(df_concat.shape[0])):
    try:
        # Extract the text from the first column of the current row
        temp_text = df_concat.iloc[i, 0]
        
        # Generate waveform from the text using the TTS model
        wav = model.generate(temp_text)
        
        # Save the generated waveform as a .wav file
        ta.save(f"", wav, model.sr)

    except Exception as e:
        # Print error information if generation or saving fails
        print(f"[❌ Error at index {i}] Text: {temp_text}")
        print(f"    → Error: {e}")
        print(wav.shape)  # Print the shape of the waveform for debugging


