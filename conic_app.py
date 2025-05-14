import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="이차방정식 도형 분류기", layout="centered")

st.title("일반형 이차방정식 도형 분류 및 그래프 시각화")

# 사용자 입력
A = st.number_input("A 계수", value=1.0)
B = st.number_input("B 계수", value=0.0)
C = st.number_input("C 계수", value=1.0)
D = st.number_input("D 계수", value=0.0)
E = st.number_input("E 계수", value=0.0)
F = st.number_input("F 계수", value=-4.0)

def classify_conic(A, B, C):
    delta = B**2 - 4*A*C
    if delta < 0 and B == 0 and A == C:
        return "원"
    elif delta < 0:
        return "타원"
    elif delta == 0:
        return "포물선"
    elif delta > 0:
        return "쌍곡선"
    else:
        return "분류 불가"

if st.button("도형 분류 및 그래프 출력"):
    conic_type = classify_conic(A, B, C)
    st.subheader(f"도형 분류 결과: {conic_type}")

    # 그래프 그리기
    x = np.linspace(-20, 20, 400)
    y = np.linspace(-20, 20, 400)
    X, Y = np.meshgrid(x, y)
    Z = A*X**2 + B*X*Y + C*Y**2 + D*X + E*Y + F

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.contour(X, Y, Z, levels=[0], colors='blue')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(f"{conic_type} 그래프", fontsize=12)
    ax.set_aspect('equal')
    ax.grid(True)
    st.pyplot(fig)
