import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🔮 Previsão Aviator", layout="centered")

# Estilo escuro
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.stApp {
    background-color: #0e1117;
}
</style>
""", unsafe_allow_html=True)

# Título
st.title("✈️ Aviator: Previsão de Multiplicadores")

st.write("Veja abaixo as previsões e o gráfico com os últimos multiplicadores simulados.")

# Função de previsão
def prever_multiplicador():
    return round(random.uniform(1.0, 50.0), 2)

# Simular histórico
historico = [round(random.uniform(1.0, 50.0), 2) for _ in range(10)]

# Mostrar gráfico
st.subheader("📊 Últimos Multiplicadores (Simulados)")
df = pd.DataFrame(historico, columns=["Multiplicador"])
df["Rodada"] = range(1, 11)

fig, ax = plt.subplots()
cores = ['green' if x >= 10 else 'red' for x in df["Multiplicador"]]
ax.bar(df["Rodada"], df["Multiplicador"], color=cores)
ax.set_xlabel("Rodada")
ax.set_ylabel("Multiplicador")
ax.set_title("Histórico de Entradas")
st.pyplot(fig)

# Previsão nova
st.subheader("🔮 Próxima Previsão")
proximo = prever_multiplicador()
st.metric("Multiplicador Estimado", f"{proximo}x", delta=None)

# Desempenho (simples)
acertos = sum(1 for m in historico if m >= 10)
st.write(f"🎯 Entradas Altas (≥10x): {acertos} de 10")
