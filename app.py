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

st.markdown(
    """
    <style>
    /* 전체 글자 색 */
    html, body, [class*="css"]  {
        color: white;
    }

    /* 본문 텍스트 */
    p {
        color: white;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
        font-size: 1.05rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .snowflake {
        position: fixed;
        top: -10px;
        color: white;
        font-size: 1em;
        user-select: none;
        pointer-events: none;
        z-index: 9999;
        animation-name: fall;
        animation-timing-function: linear;
    }

    @keyframes fall {
        to {
            transform: translateY(110vh);
        }
    }
    </style>

    <script>
    const snowflakes = 40;

    for (let i = 0; i < snowflakes; i++) {
        let snow = document.createElement("div");
        snow.className = "snowflake";
        snow.innerHTML = "❄";
        snow.style.left = Math.random() * 100 + "vw";
        snow.style.fontSize = (Math.random() * 10 + 10) + "px";
        snow.style.animationDuration = (Math.random() * 5 + 5) + "s";
        snow.style.opacity = Math.random();
        document.body.appendChild(snow);
    }
    </script>
    """,
    unsafe_allow_html=True
)
