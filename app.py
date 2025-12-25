import streamlit as st
from pathlib import Path

st.set_page_config(page_title="🎄 Christmas Carol", page_icon="🎄")

st.title("𝙲𝚑𝚛𝚒𝚜𝚝𝚖𝚊𝚜 𝚊𝚝 𝙷𝚘𝚐𝚠𝚊𝚛𝚝𝚜")
st.write("숙제하기 싫어서 만든 뻘짓거리♡꙼̈")

audio_path = Path(__file__).parent / "asset" / "carol.mp3"

if audio_path.exists():
    st.audio(audio_path.read_bytes(), format="audio/mp3")
else:
    st.error("asset/carol.mp3 파일이 없어요!")

import streamlit as st
from pathlib import Path

# 파일 경로
BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "asset"
BG_IMAGE = ASSET_DIR / "christmas.jpg"

# 배경 이미지 CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{BG_IMAGE.read_bytes().hex()}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
