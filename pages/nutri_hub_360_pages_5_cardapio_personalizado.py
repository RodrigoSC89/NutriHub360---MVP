import streamlit as st

st.title("📋 Sugestão de Cardápio")

objetivo = st.selectbox("Objetivo do paciente", ["Emagrecimento", "Hipertrofia", "Saúde geral"])
restricao = st.text_input("Restrições alimentares")

if st.button("Gerar cardápio"):
    if objetivo == "Emagrecimento":
        st.write("Café da manhã: Vitamina de banana + 1 fatia de pão integral com cottage")
        st.write("Almoço: Frango grelhado + arroz integral + salada verde")
    elif objetivo == "Hipertrofia":
        st.write("Café da manhã: Omelete com 3 ovos + tapioca")
        st.write("Almoço: Carne magra + batata doce + brócolis")
    else:
        st.write("Café da manhã: Frutas + iogurte natural + aveia")
        st.write("Almoço: Peixe grelhado + quinoa + legumes cozidos")
