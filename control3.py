import streamlit as st

st.title("Mickey poderoso")
st.header("El mas poderoso")
st.subheader("de la ciudad")
st.text("Comming 2025")
st.markdown("Texto en formato exotico")

st.sidebar.image("MICKEY.jpg")

primernum = st.sidebar.text_input("Ingrese un numero")
segundonum = st.sidebar.text_input("Ingrese otro numero")
st.sidebar.write("La multiplicacion es:",primernum*segundonum)
