import streamlit as st
import random

st.set_page_config(page_title="Previsão Aviator", layout="centered", initial_sidebar_state="collapsed")

# Estilo dark personalizado
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .stApp { background-color: #0e1117; }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 Previsão de Multiplicadores - Aviator")
st.write("Veja a previsão de entradas e acompanhe estatísticas de acertos.")

# Simulação de previsão
def prever_multiplicador():
    return round(random.uniform(2.0, 50.0), 2)

# Histórico de previsões
if "historico" not in st.session_state:
    st.session_state.historico = []

# Nova previsão
if st.button("🔮 Gerar Previsão"):
    novo = prever_multiplicador()
    st.session_state.historico.append(novo)

# Estatísticas
if st.session_state.historico:
    acertos = len([x for x in st.session_state.historico if x >= 2])
    total = len(st.session_state.historico)
    st.metric("✅ Acertos (>=2x)", f"{acertos}/{total}")
    st.line_chart(st.session_state.historico)

    st.subheader("📜 Histórico de Previsões")
    st.write(st.session_state.historico)
else:
    st.info("Clique no botão acima para gerar sua primeira previsão.")
  
