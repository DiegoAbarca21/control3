import streamlit as st
import numpy as np

st.title("Mickey poderoso")
st.header("El mas poderoso")
st.subheader("de la ciudad")
st.text("Comming 2025")
st.markdown("Texto en formato exotico")

st.sidebar.image("MICKEY.jpg")

primernum = st.sidebar.text_input("Ingrese un numero")
segundonum = st.sidebar.text_input("Ingrese otro numero")

try:
  primernum = int(primernum)
  segundonum = int(segundonum)
  numeros = np.array([primernum, segundonum])
  resultado = np.prod(numeros)
  st.sidebar.write("La multiplicacion es:", resultado)
except ValueError:
  st.sidebar.write("Por favor, ingrese números válidos.")

df = pd.DataFrame(np.random.randn(25,10))
st.dataframe(df)
