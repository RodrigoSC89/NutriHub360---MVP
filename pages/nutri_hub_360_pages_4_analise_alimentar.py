import streamlit as st
import matplotlib.pyplot as plt

st.title("🍽️ Análise Alimentar (Recordatório de 24h)")

alimentos = st.text_area("Descreva os alimentos consumidos nas últimas 24h")

if st.button("Analisar ingestão"):
    calorias = 1800  # valor fictício para o MVP
    labels = ['Carboidratos', 'Proteínas', 'Gorduras']
    sizes = [50, 25, 25]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    st.success(f"Ingestão calórica estimada: {calorias} kcal")
