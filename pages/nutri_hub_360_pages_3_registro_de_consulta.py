import streamlit as st

st.title("📝 Registro de Consulta")

st.text_input("Nome do paciente")
st.date_input("Data da consulta")
st.text_area("Sintomas relatados")
st.text_area("Exames analisados")
st.text_area("Recomendações nutricionais")

st.button("Salvar registro")
