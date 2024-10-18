import streamlit as st 
import matplotlib.pyplot as plt 
import numpy as np 
import os
import matplotlib.font_manager as fm  

# 중복되지 않고 유일한 값을 반환합니다.
def unique(list):
    x = np.array(list)
    return np.unique(x)

# 폰트를 등록합니다.
font_dirs = [os.getcwd() + '/fonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

# 폰트 매니저에 찾은 폰트를 추가합니다.
for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
fontNames = [f.name for f in fm.fontManager.ttflist]

# 기본 폰트를 NanumBarunpen으로 설정합니다.
fontname = 'NanumBarunpen'

# 선택한 폰트로 설정합니다.
plt.rc('font', family=fontname)

st.title("똘똘이 스머프에게")
st.header("우왕 이거 짱 신기하다")
st.markdown("AI강의에서 웹페이지로 배포하는것도 가르쳐주길래 테스트로 한번 해봄  \n잘 보이면 따봉 눌러줘ㅋ")

# 버튼 클릭 횟수 초기화
if 'button_count' not in st.session_state:
    st.session_state.button_count = 0

# 버튼 클릭 시 카운트 증가
if st.button('따봉을 눌러보아요👍'):
    st.session_state.button_count += 1
    st.success(f"{st.session_state.button_count}번째 따봉!")

st.selectbox('오 이건 라벨이래',['우왕','이거','짱','신기해'])

user_input = st.text_input("도색도색")

# 사용자가 입력한 값 확인
if user_input:
    if user_input == "도색도색":
        st.success("도색도색!🐽")
    else:
        st.success("아니야 그게 아니야")

image_path = os.path.join(os.getcwd(), "33.jpg")  # 이미지 파일 경로
st.image(image_path, use_column_width=True)
