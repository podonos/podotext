import torch
import torchaudio
import pandas as pd
from tqdm import tqdm
from transformers import Wav2Vec2Processor, HubertForCTC

# device setting
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# HuBERT model download
model_id = "facebook/hubert-xlarge-ls960-ft"
processor = Wav2Vec2Processor.from_pretrained(model_id)
model = HubertForCTC.from_pretrained(
    model_id,
    cache_dir=""
).to(device)


def make_asr_script(file_path):
    # load audio
    wav, sr = torchaudio.load(file_path)
    if sr != 16000:
        wav = torchaudio.functional.resample(wav, sr, 16000)
    if wav.shape[0] > 1:  # stereo → mono
        wav = torch.mean(wav, dim=0, keepdim=True)

    input_values = processor(wav.squeeze().numpy(), return_tensors="pt", sampling_rate=16000).input_values.to(device)


    with torch.no_grad():
        logits = model(input_values).logits

    # CTC Greedy Decoding
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    return transcription


def make_asr(tts_model, data_domain):
    print(f"{tts_model} start")
    df_tts = pd.read_csv(f"") # csv url to generate wav file

    scription_list = []
    for i in tqdm(range(df_tts.shape[0])):
        temp_url = df_tts.iloc[i, 6]  # wav file url link
        scription_temp = make_asr_script(temp_url)
        scription_list.append(scription_temp)

    # save transcription file
    if df_tts.shape[0] == len(scription_list):
        df_tts["hubert"] = scription_list

    df_tts.to_csv(
        f"",
        index=False,
        encoding="utf-8-sig"
    )


# make transcription file 4 tts model
make_asr("chatterbox", "medicine")
make_asr("kokoro", "medicine")
make_asr("mello", "medicine")
make_asr("higgs", "medicine")
