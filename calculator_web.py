import streamlit as st

st.title("かんたん電卓")

a = st.number_input("最初の数字", value=0.0)
b = st.number_input("次の数字", value=0.0)

st.write("---")
st.write(f"{a} ＋ {b} = **{a + b}**")
st.write(f"{a} ー {b} = **{a - b}**")
st.write(f"{a} × {b} = **{a * b}**")

if b != 0:
    st.write(f"{a} ÷ {b} = **{a / b:.4f}**")
else:
    st.warning("÷ 0 は計算できません")
