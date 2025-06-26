"""
Text-to-Speech Generation Script using OutetTS

- Model: OutetTS (Version 1.0, size 0.6B)
- GitHub or Source: https://github.com/edwko/OuteTTS 
- Language: English (EN-FEMALE-1-NEUTRAL speaker)
- Requirements:
    - outetts
    - pandas
    - tqdm
    - GPU or CPU (model auto-configures backend)
"""

# Import necessary libraries
from outetts import (
    Interface, ModelConfig, GenerationConfig,
    Backend, InterfaceVersion, Models, GenerationType
)
import pandas as pd
import os
from tqdm import tqdm  


# Initialize the TTS interface with the OutetTS model (version 1.0, 0.6B size)
interface = Interface(
    ModelConfig.auto_config(
        model=Models.VERSION_1_0_SIZE_0_6B,
        backend=Backend.HF,  # Uses HuggingFace backend
    )
)

# Load the default English speaker (neutral female voice)
speaker = interface.load_default_speaker("EN-FEMALE-1-NEUTRAL")

# Load input text data from CSV file
df_concat = pd.read_csv("")

# Iterate through each sentence and synthesize speech
for i in tqdm(range(df_concat.shape[0])):
    try:
        # Extract the sentence text from the DataFrame
        temp_text = df_concat.iloc[i, 0]
        
        # Generate audio using the TTS interface
        output = interface.generate(
            GenerationConfig(
                text=temp_text,
                speaker=speaker,
            )
        )
        
        # Save the synthesized audio to a .wav file
        output.save(f"")

    except Exception as e:
        # Print error details if generation fails
        print(f"[❌ Error at index {i}] Text: {temp_text}")
        print(f"    → Error: {e}")
