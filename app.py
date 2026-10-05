import streamlit as st

st.title("課題管理")

memo = st.text_area("メモ")

st.write(memo)
