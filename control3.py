import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title("Mickey poderoso")
st.header("El más poderoso")
st.subheader("de la ciudad")
st.text("Coming 2025")
st.markdown("Texto en formato exótico")

st.sidebar.image("MICKEY.jpg")

primernum = st.sidebar.text_input("Ingrese un número")
segundonum = st.sidebar.text_input("Ingrese otro número")

try:
    primernum = int(primernum)
    segundonum = int(segundonum)
    numeros = np.array([primernum, segundonum])
    resultado = np.prod(numeros)
    st.sidebar.write("La multiplicación es:", resultado)
except ValueError:
    st.sidebar.write("Por favor, ingrese números válidos.")

df = pd.DataFrame(np.random.randn(25, 30), columns=[f'Columna {i}' for i in range(30)])
st.dataframe(df)

x_data = df.iloc[:, 0]
y_data = df.iloc[:, 1]

fig, ax = plt.subplots(figsize=(10, 5))

ax.scatter(x_data, y_data, color='lightgreen', edgecolor="black")

ax.set_xlabel("Primera Columna")
ax.set_ylabel("Segunda Columna")
ax.set_title('Gráfico de Dispersión')
st.header("Un grafico hecho con plt")
st.pyplot(fig)

chart = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X(df.columns[0], title="Primera Columna"),  # Usar el nombre de la primera columna
    y=alt.Y(df.columns[1], title="Segunda Columna"),  # Usar el nombre de la segunda columna
    tooltip=[df.columns[0], df.columns[1]]  # Mostrar los valores de las columnas en los tooltips
).interactive()

st.header("El mismo grafico hecho con altair")

st.altair_chart(chart, use_container_width=True)

bar_chart = alt.Chart(df).mark_bar(color='lightgreen', size=25,stroke="black",strokeWidth=2).encode(
    x=alt.X('Columna 1', title='Primera Columna'),
    y=alt.Y('Columna 2', title='Segunda Columna'),
    tooltip=['Columna 1', 'Columna 2']
).interactive()

# Mostrar el gráfico de barras en Streamlit
st.altair_chart(bar_chart, use_container_width=True)
