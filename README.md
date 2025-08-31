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
