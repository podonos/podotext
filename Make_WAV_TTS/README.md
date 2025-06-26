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

> ⚙️ To use these models, please make sure to install the corresponding libraries provided on each Hugging Face model page.
