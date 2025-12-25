import streamlit as st
from pathlib import Path

st.set_page_config(page_title="🎄 Christmas Carol", page_icon="🎄")

st.title("🎄 크리스마스 캐롤 웹페이지")
st.write("아이패드로 만든 Streamlit 페이지")

audio_path = Path(__file__).parent / "assets" / "carol.mp3"

if audio_path.exists():
    st.audio(audio_path.read_bytes(), format="audio/mp3")
else:
    st.error("assets/carol.mp3 파일이 없어요!")
