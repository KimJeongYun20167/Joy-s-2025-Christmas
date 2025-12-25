import streamlit as st
from pathlib import Path

st.set_page_config(page_title="🎄 Christmas Carol", page_icon="🎄")

st.title("𝙲𝚑𝚛𝚒𝚜𝚝𝚖𝚊𝚜 𝚊𝚝 𝙷𝚘𝚐𝚠𝚊𝚛𝚝𝚜")
st.write("숙제하기 싫어서 만든 뻘짓거리♡꙼̈")

audio_path = Path(__file__).parent / "asset" / "carol.mp3"

if audio_path.exists():
    st.audio(audio_path.read_bytes(), format="audio/mp3")
else:
    st.error("assets/carol.mp3 파일이 없어요!")
