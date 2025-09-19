# 🗂️ Podo Text: DOMAIN-SPECIFIC TEXT DATASET FOR TEXT-TO-SPEECH BENCHMARK


**PodoText** is a domain-specific text dataset designed for benchmarking Text-to-Speech (TTS) and Automatic Speech Recognition (ASR) systems. It was created using both fine-tuning and prompting approaches on large language models (LLMs) to generate high-quality, domain-relevant text.

## 📌 Overview

This repository contains:

- A synthetic evaluation dataset of 10,000 domain-specific sentences was constructed by sampling:
  - 2,000 sentences each from: **medical**, **addresses**, **celebrities**, and **sport players**
  - 1,000 sentences each from: **legal** and **banking**- Sample scripts for **TTS inference** and **ASR transcription**.
- ✅ This **10,000-sentence evaluation set** used in our experiments is **publicly available** in this repository.
- Benchmark results (WER/CER) across multiple open-source models.


## 🧠 Key Features

- **6 Domains**: Medical, Addresses, Sports Players, Celebrities, Banking, Legal  
- **Data Sources**: ChatGPT-4o, Gemini API, DrugBank, OpenAddresses, IMDb, etc.
- **Text Generation Methods**:
  - **Fine-tuning** 
  - **Prompting** 
  - 4 TTS models: Kokoro, Chatterbox, Higgs, MeloTTS
  - 4 ASR models: Whisper, Wav2Vec2, Parakeet, Hubert
  - Evaluation metrics: WER, CER


## 🔗 Related Resources

**🗣️ Text-to-Speech (TTS) Models**
- [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- [Chatterbox](https://huggingface.co/ResembleAI/chatterbox)
- [MeloTTS](https://huggingface.co/myshell-ai/MeloTTS-English)
- [Higgs](https://huggingface.co/bosonai/higgs-audio-v2-generation-3B-base)

**🎧 Automatic Speech Recognition (ASR) Models**
- [Whisper (whisper-large-v3-turbo)](https://huggingface.co/openai/whisper-large-v3-turbo)
- [Parakeet (parakeet-tdt-0.6b-v2)](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2)
- [Wav2Vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h)
- [Hubert (hubert-xlarge-ls960-ft)](https://huggingface.co/facebook/hubert-xlarge-ls960-ft)

Each TTS model synthesized 10,000 audio samples from the dataset, and each ASR model transcribed those audio files. We calculated Word Error Rate (WER) and Character Error 

---

🎙️**Human Speech Recordings**

We collected **human-recorded speech samples** aligned with the same text prompts to enable direct comparison with TTS-generated outputs.

- **Total Samples**: 1,800  
  - **1,000 samples** from the *medical* domain  
  - **200 samples each** from *addresses*, *celebrities*, *sports players*  
  - **100 samples each** from *banking* and *legal* domains  

- **Domain-Specific Requirement (Medical)**:  
  - For the medical domain, recordings were restricted to participants with **professional backgrounds** (e.g., doctors, nurses, pharmacists)  
  - This ensured **accurate and domain-appropriate pronunciations** of specialized terms

- **Usage**:  
  - Human recordings were used to **compare performance** with TTS-generated speech  
  - They were also employed to **fine-tune ASR models** in the medical domain

## 🧪 Experiments

To evaluate the effectiveness of the PodoText dataset, we conducted benchmark experiments using four open-source TTS models and three ASR models. The goal was to assess how well ASR systems transcribe speech synthesized from domain-specific texts.

### 🎯 Evaluation Setup

- **Evaluation Dataset**: 10,000 sampled sentences  
  (2,000 each from `medical`, `addresses`, `celebrities`, `sport players`; 1,000 each from `legal`, `banking`)
- **TTS Models**:
  - Kokoro-82M
  - Chatterbox
  - MeloTTS
  - Higgs
- **ASR Models**:
  - Whisper (large-v3-turbo)
  - Wav2Vec2-base-960h
  - Parakeet-TDT
  - Hubert (hubert-xlarge-ls960-ft)
- **Metrics**: Word Error Rate (WER), Character Error Rate (CER)



## Results

### Human vs. TTS Speech
- *Comparison of WER and CER between human-recorded speech and TTS-generated speech across six domains.*  
- Human speech consistently achieved lower error rates, while some TTS models (e.g., Kokoro) showed reduced CER by spelling out OOV words.

<img width="1274" height="621" alt="image" src="https://github.com/user-attachments/assets/838348d0-99c0-49be-a53a-82a4b41fe430" />




---

### Error Rate Variations Across Models
- *Comparison of error rates across different TTS and ASR models.*  
- Results show substantial performance variations depending on the TTS model and the ASR system used.
<img width="1676" height="562" alt="image" src="https://github.com/user-attachments/assets/59a6d9b4-1be3-44e4-9a82-418b1aa240a7" />

---

### Domain-Specific Results
- *WER and CER results of TTS models evaluated in each domain.*  
- Domain-specific datasets resulted in higher errors than the general-purpose LJSpeech dataset, confirming the difficulty of domain adaptation.
<img width="1674" height="833" alt="image" src="https://github.com/user-attachments/assets/847047f1-05e1-4824-923d-766e971692a6" />

---


### Medical Domain Analysis 
- *Comparison of human and TTS-generated speech specifically in the medical domain.*  
- Human speech generally showed the lowest errors, but in some cases Kokoro produced lower CER by spelling out OOV words letter-by-letter, which certain ASR models merged correctly.
<img width="1662" height="679" alt="image" src="https://github.com/user-attachments/assets/51e3f2e5-d8e8-465d-9035-fa4321c873e8" />

---

### Medical Domain Fine-Tuning
- *Effect of fine-tuning ASR models with human medical recordings.*  
- Fine-tuned ASR models showed reduced error rates for both human and TTS-generated speech, demonstrating the value of domain-specific adaptation.


<img width="1684" height="654" alt="image" src="https://github.com/user-attachments/assets/d1364da4-7445-40f3-9a86-851db7b16274" />


---

### 🔍 Key Insights

- 🗣️ **Human recordings** consistently achieved lower WER/CER than TTS-generated speech, confirming the gap between natural and synthetic speech.  
- 🔤 **Kokoro** occasionally outperformed human speech in CER by spelling out OOV terms letter-by-letter, which some ASR models merged correctly.  
- ⚖️ **Error rates varied widely** depending on both the TTS and ASR models, showing strong model-specific biases.  
- 🏷️ **Domain-specific datasets** (medical, addresses, sports, etc.) produced higher errors compared to general-purpose LJSpeech, highlighting domain difficulty.  
- 🩺 **Fine-tuning ASR models with human medical recordings** reduced WER, demonstrating the effectiveness of domain adaptation using PodoText.


---

## 📁 Dataset Structure

Each domain is organized in JSON format with annotated fields such as sentence, domain tag, or number of words.

```
Text Corpus
├── Addresses_Corpus.json
├── Bnking_Corpus.json
├── Celebrities_Corpus.json
├── Legal_Corpus.json
├── Medical_Corpus.json
├── SportPlayers_Corpus.json

```

## ✍️ Citation

```

```

## 📬 Contact

- 📧 Youngwoo Choi: ywchoi@dsp.inha.ac.kr
- 🌎 Project by [Podonos](https://podonos.com)  


