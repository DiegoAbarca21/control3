import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

df = pd.DataFrame(np.random.randn(25, 10))
st.dataframe(df)

first_column_data = df.iloc[:, 0].to_numpy()
second_column_data = df.iloc[:, 1].to_numpy()

male_count = np.sum(first_column_data > -9999999999)  
female_count = np.sum(second_column_data > -9999999999)  

fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax[0].scatter(["desde", "hasta"], [male_count, female_count], color="red")
ax[0].set_xlabel("numeros")
ax[0].set_ylabel("pickaxe")
ax[0].set_title('Distribución de hombres y mujeres')


st.pyplot(fig)
