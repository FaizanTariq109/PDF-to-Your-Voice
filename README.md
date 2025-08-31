# 🎵 Text-to-Speech Generator (GTTS + XTTS)

This project is a **Text-to-Speech (TTS) generator** that can convert a PDF book (or any text) into speech.  
It provides two modes:

1. **GTTS (Google Text-to-Speech)** – default robotic voice.  
2. **XTTS (Coqui TTS)** – AI-powered voice cloning using your own sample voice.  

Built with **Streamlit** for easy interaction.

---

## 🚀 Features
- Upload a **PDF file** or paste text directly.  
- Upload a **WAV voice sample** for cloning (XTTS).  
- Choose output type:  
  - ✅ GTTS (robotic)  
  - ✅ XTTS (cloned voice)  
  - ✅ Both  
- Adjustable parameters:
  - `CHUNK_SIZE` – Characters per chunk (default: 200).  
  - `MAX_CHUNKS` – Limit number of chunks/pages (default: 20).  
- Real-time progress updates in UI.  
- Generated audio is playable in the browser.  

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/text-to-speech-generator.git
cd text-to-speech-generator

Run Streamlit:
streamlit run script.py

## 🎤 How It Works

1. 📑 Upload a **PDF file**.  
2. 🎛️ Choose between **gTTS (Google’s TTS)** or **XTTS (voice cloning)**.  
3. 🧑‍🤝‍🧑 For **XTTS**, upload a short **voice sample (WAV format)**.  
4. ⏳ Wait while **chunks are processed into speech**.  
5. 🎶 Listen or **download your personalized audiobook**.  

---

## ✨ Demo

- 🔗 **App**: [PDF to Your Voice - Streamlit](https://faizantariq109-pdf-to-your-voice-script-lhgge7.streamlit.app/)  
- 🔗 **Blog**: [Medium Article](https://medium.com/@faizan3san/%EF%B8%8F-building-a-text-to-speech-app-with-gtts-and-xtts-voice-cloning-58ae57003337)  

---

## 📌 Roadmap

- [ ] 🌍 Support for **multiple languages**.  
- [ ] 📊 Add **UI progress bar** during audio generation.  
- [ ] 🎙️ Option to select **different cloned voices**.  

---

## 🤝 Contributing

Pull requests are welcome!  
If you’d like to **improve features**, **add screenshots**, or **optimize audio processing** — feel free to fork and submit.  
