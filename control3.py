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
primernum.astype(int)
segundonum.astype(int)
primersegundonum = np.array([primernum,segundonum])
nummult = np.prod(primersegundonum)
nummult.astype(str)
st.sidebar.write("La multiplicacion es:", nummult)
