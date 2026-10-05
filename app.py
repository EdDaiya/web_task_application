import streamlit as st

st.title("課題管理")


subject = st.text_input("科目")
task = st.text_input("課題名")
deadline = st.data_input("提出期限")

if st.button("課題を追加")
    st.write("課題を追加しました")
