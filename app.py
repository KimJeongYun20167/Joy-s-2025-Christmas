import streamlit as st
from pathlib import Path
import base64
import random

st.set_page_config(page_title="🎄 Christmas Carol", page_icon="🎄", layout="centered")

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "asset"

# 배경
# =====================
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

# =====================
# 글씨 흰색 강제
# =====================
st.markdown(
    """
    <style>
    .stApp, .stApp * { color: white !important; }
    .stApp h1 { color: white !important; font-weight: 700 !important; }
    .stApp p  { color: white !important; font-size: 1.05rem !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================
# ❄️ 눈 내리는 효과
# =====================
def make_snow_html(n: int = 60) -> str:
    flakes = []
    for _ in range(n):
        left = random.uniform(0, 100)
        size = random.uniform(10, 20)
        duration = random.uniform(6, 12)
        delay = random.uniform(0, 6)
        opacity = random.uniform(0.3, 1.0)
        flakes.append(
            f'<span class="snowflake" style="left:{left:.2f}vw; font-size:{size:.2f}px; '
            f'animation-duration:{duration:.2f}s; animation-delay:-{delay:.2f}s; opacity:{opacity:.2f};">❄</span>'
        )

    return f"""
    <style>
    #snow-layer {{ position: fixed; inset: 0; pointer-events: none; z-index: 9999; overflow: hidden; }}
    .snowflake {{
        position: absolute; top: -30px; color: white; user-select: none;
        animation-name: snow-fall; animation-timing-function: linear; animation-iteration-count: infinite;
        will-change: transform;
    }}
    @keyframes snow-fall {{
        0%   {{ transform: translateY(-40px); }}
        100% {{ transform: translateY(110vh); }}
    }}
    </style>
    <div id="snow-layer">{''.join(flakes)}</div>
    """

st.markdown(make_snow_html(), unsafe_allow_html=True)

# =====================
import requests

NAMESPACE = "christmas-at-hogwarts"   # 아무 문자열, 앱마다 고유하게
KEY = "total-visits"

try:
    r = requests.get(f"https://api.countapi.xyz/hit/{NAMESPACE}/{KEY}", timeout=5)
    total = r.json().get("value", "?")

    st.markdown(
        f"""
        <div style="
            display:inline-block;
            background: rgba(0,0,0,0.45);
            padding: 10px 14px;
            border-radius: 12px;
            margin-bottom: 10px;
            font-weight: 700;
        ">
            👀 Visitors at Hogwarts: {total}
        </div>
        """,
        unsafe_allow_html=True
    )
except:
    st.markdown("👀 Visitors at Hogwarts: ?")
# =====================
# 본문
# =====================
st.title("Christmas at Hogwarts")
st.write("숙제하기 싫어서 만든 뻘짓거리♡꙼̈")

audio_path = ASSET_DIR / "carol.mp3"
if audio_path.exists():
    st.audio(audio_path.read_bytes())
else:
    st.error("asset/carol.mp3 파일이 없어요!")
