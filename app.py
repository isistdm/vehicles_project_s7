import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Vehículos - Proyecto S7')

# Encabezado del histograma
st.subheader('Distribución del odómetro')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=df['odometer'])])

    # Título para el gráfico
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, width='stretch')

# Encabezado del histograma
st.subheader('Gráfico de dispersión del precio vs año del modelo')

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs año del modelo')
    fig = go.Figure(data=[go.Scatter(
        x=df['model_year'], 
        y=df['price'], 
        mode='markers',
        marker=dict(opacity=0.6)
    )])
    
    fig.update_layout(
        title_text='Precio vs Año del Modelo',
        xaxis=dict(title='Año del Modelo'),
        yaxis=dict(title='Precio')
    )

    st.plotly_chart(fig, width='stretch')
 