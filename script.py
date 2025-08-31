import streamlit as st
import os
import tempfile
from PyPDF2 import PdfReader
from gtts import gTTS
from TTS.api import TTS

# --------------------
# CONFIGURABLE VALUES
# --------------------
CHUNK_SIZE = 200     # characters per chunk
MAX_CHUNKS = 20      # limit for testing
START_PAGE = 1       # starting page (1-indexed)
END_PAGE = 5         # ending page
LANGUAGE = "en"      # default language

# --------------------
# HELPERS
# --------------------
def extract_text_from_pdf(pdf_file, start_page=1, end_page=5):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page_num in range(start_page-1, min(end_page, len(pdf_reader.pages))):
        text += pdf_reader.pages[page_num].extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=CHUNK_SIZE, max_chunks=MAX_CHUNKS):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
        if len(chunks) >= max_chunks:
            break
    return chunks

def generate_gtts(chunks, output_file):
    with open(output_file, "wb") as f:
        for i, chunk in enumerate(chunks):
            tts = gTTS(text=chunk, lang=LANGUAGE)
            tts.write_to_fp(f)

def generate_xtts(chunks, output_file, voice_path):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    with open(output_file, "wb") as f:
        for i, chunk in enumerate(chunks):
            tts.tts_to_file(
                text=chunk,
                file_path=output_file,
                speaker_wav=voice_path,
                language=LANGUAGE
            )

# --------------------
# STREAMLIT APP
# --------------------
st.title("📖 PDF to Audiobook Converter")

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
voice_file = st.file_uploader("Upload your voice sample (wav/mp3)", type=["wav", "mp3"])

choice = st.multiselect("Choose output type(s):", ["GTTS (default voice)", "XTTS (your cloned voice)"], default=["GTTS (default voice)"])

# Editable parameters
CHUNK_SIZE = st.number_input("Chunk Size (characters)", value=200)
MAX_CHUNKS = st.number_input("Max Chunks", value=20)
START_PAGE = st.number_input("Start Page", value=1)
END_PAGE = st.number_input("End Page", value=5)

if st.button("Generate Audiobook") and pdf_file is not None:
    text = extract_text_from_pdf(pdf_file, START_PAGE, END_PAGE)
    chunks = chunk_text(text, CHUNK_SIZE, MAX_CHUNKS)

    if not chunks:
        st.error("No text extracted from the PDF.")
    else:
        if "GTTS (default voice)" in choice:
            gtts_file = "audiobook_gtts.mp3"
            generate_gtts(chunks, gtts_file)
            st.success("✅ GTTS audiobook generated!")
            st.audio(gtts_file)

        if "XTTS (your cloned voice)" in choice:
            if voice_file is None:
                st.error("Please upload a voice sample for XTTS.")
            else:
                # save uploaded file to temp .wav
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(voice_file.read())
                    voice_path = tmp.name

                xtts_file = "audiobook_xtts.wav"
                generate_xtts(chunks, xtts_file, voice_path)
                st.success("✅ XTTS audiobook generated with your cloned voice!")
                st.audio(xtts_file)