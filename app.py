import streamlit as st
from streamlit_mic_recorder import mic_recorder

from services.speech_to_text import transcribe_audio
from services.translator import translate
from services.llm import generate_response
from services.tts import text_to_speech
import os

os.makedirs("audio", exist_ok=True)

st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎙️"
)

st.title("🎙️ AI Voice Assistant")

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="recorder"
)

if audio:

    with open("audio/question.wav", "wb") as f:
        f.write(audio["bytes"])
        
    st.markdown("### 👤 You")
    st.audio(audio["bytes"])

    if st.button("Send"):

        with st.spinner("Thinking..."):

            text, language = transcribe_audio(
                "audio/question.wav"
            )

            

            
            prompt=translate(text,language)
            

            response = generate_response(
                prompt
            )
            
            response=translate(response,language)
            
            
            
            

            audio_file = text_to_speech(
                response,
                language
            )
            st.markdown("### 🤖 Assistant")
            st.audio(audio_file)