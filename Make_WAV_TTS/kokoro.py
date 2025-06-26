"""
Text-to-Speech Generation Script using Kokoro TTS

- Model: Kokoro TTS (via KPipeline)
- GitHub Repository: https://github.com/hexgrad/kokoro 
- Voice: 'af_heart' voice is used for generation
- Requirements:
    - kokoro (with KPipeline)
    - soundfile
    - pandas
    - tqdm
    - PyTorch
    - GPU recommended for faster inference
"""


# Import necessary libraries
from kokoro import KPipeline                    
from IPython.display import display, Audio      
import soundfile as sf                          
import torch
import pandas as pd                             
import os

# Initialize the Kokoro TTS pipeline with a specific language code
pipeline = KPipeline(lang_code='a')

# Load the text data from a CSV file
df_concat = pd.read_csv("")

from tqdm import tqdm  # Progress bar for iteration

# Loop through each sentence in the DataFrame
for i in tqdm(range(df_concat.shape[0])):
    try:
        # Get the sentence text from the first column
        temp_text = df_concat.iloc[i, 0]

        # Generate speech using the 'af_heart' voice
        generator = pipeline(temp_text, voice='af_heart')

        # The generator yields audio outputs (possibly multi-segment)
        for k, (gs, ps, audio) in enumerate(generator):
            # Save the generated audio as a .wav file with 24kHz sample rate
            sf.write(f'', audio, 24000)

    except Exception as e:
        # If any error occurs, print the index and error message
        print(f"[❌ Error at index {i}] Text: {temp_text}")
        print(f"    → Error: {e}")
