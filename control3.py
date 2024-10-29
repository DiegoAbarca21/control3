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

# Extraer los datos de las primeras dos columnas
first_column_data = df.iloc[:, 0].to_numpy()
second_column_data = df.iloc[:, 1].to_numpy()

# Crear una figura con un solo gráfico
fig, ax = plt.subplots(1, 1, figsize=(10, 3))

# Agregar los datos al gráfico
ax.plot(["Masculino", "Femenino"], [np.sum(first_column_data > 0), np.sum(second_column_data > 0)], color="red")
ax.set_xlabel("Sexo")
ax.set_ylabel("Cantidad")
ax.set_title('Distribución de hombres y mujeres')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
