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

x_data = df.iloc[:, 0].to_numpy()  # Primera columna
y_data = df.iloc[:, 1].to_numpy()  # Segunda columna

# Crear una figura con un solo gráfico
fig, ax = plt.subplots(figsize=(10, 5))

# Crear el scatter plot
ax.scatter(x_data, y_data, color='blue', alpha=0.6)

# Configurar los ejes y el título
ax.set_xlabel("Primera Columna")
ax.set_ylabel("Segunda Columna")
ax.set_title('Gráfico de Dispersión')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
