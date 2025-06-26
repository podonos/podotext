# 🗂️ PodoText: Domain-Specific Text Dataset for Speech Synthesis Using LLM-Based Text Generation


**PodoText** is a domain-specific text dataset designed for benchmarking Text-to-Speech (TTS) and Automatic Speech Recognition (ASR) systems. It was created using both fine-tuning and prompting approaches on large language models (LLMs) to generate high-quality, domain-relevant text.

## 📌 Overview

This repository contains:

- A synthetic evaluation dataset of 10,000 domain-specific sentences was constructed by sampling:
  - 2,000 sentences each from: **medical**, **addresses**, **celebrities**, and **sport players**
  - 1,000 sentences each from: **legal** and **banking**- Sample scripts for **TTS inference** and **ASR transcription**.
- Benchmark results (WER/CER) across multiple open-source models.


## 🧠 Key Features

- **6 Domains**: Medical, Addresses, Sport Players, Celebrities, Banking, Legal  
- **Data Sources**: ChatGPT-4o, Gemini API, DrugBank, OpenAddresses, IMDb, etc.
- **Text Generation Methods**:
  - **Fine-tuning** 
  - **Prompting** 
  - 4 TTS models: Kokoro, Chatterbox, OuteTTS, MeloTTS
  - 3 ASR models: Whisper, Wav2Vec2, Parakeet
  - Evaluation metrics: WER, CER


## 🔗 Related Resources

**🗣️ Text-to-Speech (TTS) Models**
- [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- [Chatterbox](https://huggingface.co/ResembleAI/chatterbox)
- [OuteTTS-1.0-0.6B](https://huggingface.co/OuteAI/OuteTTS-1.0-0.6B)
- [MeloTTS](https://huggingface.co/myshell-ai/MeloTTS-English)

**🎧 Automatic Speech Recognition (ASR) Models**
- [Whisper (whisper-large-v3-turbo)](https://huggingface.co/openai/whisper-large-v3-turbo)
- [Parakeet (parakeet-tdt-0.6b-v2)](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2)
- [Wav2Vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h)

Each TTS model synthesized 10,000 audio samples from the dataset, and each ASR model transcribed those audio files. We calculated Word Error Rate (WER) and Character Error Rate (CER) for evaluation.

## 🧪 Experiments

To evaluate the effectiveness of the PodoText dataset, we conducted benchmark experiments using four open-source TTS models and three ASR models. The goal was to assess how well ASR systems transcribe speech synthesized from domain-specific texts.

### 🎯 Evaluation Setup

- **Evaluation Dataset**: 10,000 sampled sentences  
  (2,000 each from `medical`, `addresses`, `celebrities`, `sport players`; 1,000 each from `legal`, `banking`)
- **TTS Models**:
  - Kokoro-82M
  - Chatterbox
  - OuteTTS-1.0-0.6B
  - MeloTTS
- **ASR Models**:
  - Whisper (large-v3-turbo)
  - Wav2Vec2-base-960h
  - Parakeet-TDT
- **Metrics**: Word Error Rate (WER), Character Error Rate (CER)



### 📊 Overall WER & CER Results

<img src="https://github.com/podonos/podotext/blob/main/Table2_image.png" alt="WER AND CER RESULTS OF TTS-GENERATED SPEECH ACROSS ALL DOMAINS" width="700"/>

### 📌 WER & CER by Domain

<img src="https://github.com/podonos/podotext/blob/main/Table3_image.png" alt="WER AND CER RESULTS BY DOMAIN AND TTS MODEL" width="700"/>




### 🔍 Key Insights

- 🏆 **MeloTTS** showed the best performance on average (WER 14.7%, CER 4.6%).
- 🧠 **Whisper** consistently outperformed other ASR models.
- 🏙️ **Addresses** and **medicine** domains showed high error rates due to variability and terminology.
- 📈 These results validate the value of PodoText for benchmarking realistic, domain-specific speech systems.






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


