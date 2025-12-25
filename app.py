import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="🎄 Christmas Carol", page_icon="🎄")

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "asset"

# 배경 이미지
BG_IMAGE = ASSET_DIR / "christmas.JPG"
bg_base64 = base64.b64encode(BG_IMAGE.read_bytes()).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("𝙲𝚑𝚛𝚒𝚜𝚝𝚖𝚊𝚜 𝚊𝚝 𝙷𝚘𝚐𝚠𝚊𝚛𝚝𝚜")
st.write("숙제하기 싫어서 만든 뻘짓거리♡꙼̈")

audio_path = ASSET_DIR / "carol.mp3"

if audio_path.exists():
    st.audio(audio_path.read_bytes())
else:
    st.error("asset/carol.mp3 파일이 없어요!")
