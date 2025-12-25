
import streamlit as st
from pathlib import Path
import base64
import random

st.set_page_config(page_title="🎄 Christmas Carol", page_icon="🎄", layout="centered")

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "asset"

# =====================
# 배경 이미지
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
# 글씨 흰색 "강제" (그림자 없음)
# =====================
st.markdown(
    """
    <style>
    /* Streamlit이 덮어쓰는 걸 방지하려고 !important 사용 */
    .stApp, .stApp * {
        color: white !important;
    }

    /* 제목은 깔끔하게 흰색만 */
    .stApp h1 {
        color: white !important;
        font-weight: 700 !important;
    }

    /* 본문 */
    .stApp p {
        color: white !important;
        font-size: 1.05rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================
# ❄️ 눈 내리는 효과 (JS 없이, HTML+CSS만)
# =====================
def make_snow_html(n: int = 50) -> str:
    flakes = []
    for _ in range(n):
        left = random.uniform(0, 100)          # vw
        size = random.uniform(10, 20)          # px
        duration = random.uniform(6, 12)       # s
        delay = random.uniform(0, 6)           # s
        opacity = random.uniform(0.3, 1.0)
        # 각 눈송이를 개별 스타일로 만들어서 JS 없이도 다양하게 떨어지게 함
        flakes.append(
            f'<span class="snowflake" style="left:{left:.2f}vw; '
            f'font-size:{size:.2f}px; animation-duration:{duration:.2f}s; '
            f'animation-delay:-{delay:.2f}s; opacity:{opacity:.2f};">❄</span>'
        )

    return f"""
    <style>
    #snow-layer {{
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }}

    .snowflake {{
        position: absolute;
        top: -30px;
        color: white;
        user-select: none;
        animation-name: snow-fall;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
        will-change: transform;
    }}

    @keyframes snow-fall {{
        0%   {{ transform: translateY(-40px); }}
        100% {{ transform: translateY(110vh); }}
    }}
    </style>

    <div id="snow-layer">
        {''.join(flakes)}
    </div>
    """

st.markdown(make_snow_html(60), unsafe_allow_html=True)

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
