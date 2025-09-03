import streamlit as st
import json
import os

data_path = "data/pacientes.json"

st.title("🧑‍⚕️ Cadastro de Paciente")

nome = st.text_input("Nome completo")
idade = st.number_input("Idade", 0, 120, step=1)
sexo = st.selectbox("Sexo", ["Feminino", "Masculino", "Outro"])
peso = st.number_input("Peso (kg)", 0.0, 300.0, step=0.1)
altura = st.number_input("Altura (cm)", 0.0, 250.0, step=0.1)
objetivo = st.text_area("Objetivo nutricional")
restricoes = st.text_area("Restrições/alergias")
email = st.text_input("E-mail")

if st.button("Salvar paciente"):
    novo_paciente = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "peso": peso,
        "altura": altura,
        "objetivo": objetivo,
        "restricoes": restricoes,
        "email": email
    }
    if not os.path.exists("data"):
        os.makedirs("data")
    if os.path.exists(data_path):
        with open(data_path, "r") as f:
            dados = json.load(f)
    else:
        dados = []
    dados.append(novo_paciente)
    with open(data_path, "w") as f:
        json.dump(dados, f, indent=4)
    st.success("Paciente salvo com sucesso!")
