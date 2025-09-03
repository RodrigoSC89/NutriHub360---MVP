[nutri_hub_360_readme.txt](https://github.com/user-attachments/files/22127393/nutri_hub_360_readme.txt)
# NutriHub360 - MVP com Streamlit

## 🧠 Visão Geral
Sistema de apoio inteligente para nutricionistas, com funcionalidades como:
- Cadastro de pacientes
- Registro de consultas
- Análise de recordatórios alimentares
- Sugestão de cardápio
- Biblioteca de conteúdos educativos

---

## 🚀 Como Executar Localmente

### 1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/NutriHub360---MVP.git
cd NutriHub360---MVP
```

### 2. Crie e ative um ambiente virtual:
#### Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
#### macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências:
```bash
pip install streamlit matplotlib
```

### 4. Rode o app:
```bash
streamlit run app.py
```

---

## 📁 Estrutura de Pastas
```
NutriHub360-MVP/
├── app.py
├── README.md
├── data/
│   └── pacientes.json
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Cadastro_de_Paciente.py
│   ├── 3_Registro_de_Consulta.py
│   ├── 4_Analise_Alimentar.py
│   ├── 5_Cardapio_Personalizado.py
│   └── 6_Biblioteca.py
```

## 💡 Inspiração
Projeto MVP para apoiar a prática clínica de nutricionistas, oferecendo ferramentas simples e eficazes em um ambiente intuitivo. Desenvolvido com carinho pelo NutriXpert 360° 💚
