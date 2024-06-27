import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Generar datos falsos
def generate_fake_data(num_samples=1000):
    np.random.seed(42)
    data = {
        "current_velocity": np.random.uniform(0.1, 2.0, num_samples),
        "angle_of_attack": np.random.randint(0, 90, num_samples),
        "solidity": np.random.uniform(0.1, 0.4, num_samples),
        "twine_diameter": np.random.uniform(0.5, 5.0, num_samples),
    }
    return pd.DataFrame(data)

# Crear datos
data = generate_fake_data()

# Calcular fuerza hidrodinámica usando una fórmula simplificada
def calculate_hydrodynamic_force(row):
    return row["current_velocity"] ** 2 * row["solidity"] * row["twine_diameter"] * np.sin(np.radians(row["angle_of_attack"]))

data["hydrodynamic_force"] = data.apply(calculate_hydrodynamic_force, axis=1)

# Configurar la página de Streamlit
st.title("Simulación Hidrodinámica para Redes de Acuicultura")

# Control deslizante para el ángulo de ataque
angle = st.slider("Ángulo de ataque", min_value=0, max_value=90, step=1)

# Definir un rango pequeño alrededor del ángulo seleccionado
angle_range = 2  # Puedes ajustar este valor según sea necesario
filtered_data = data[(data["angle_of_attack"] >= angle - angle_range) & (data["angle_of_attack"] <= angle + angle_range)]

# Crear y mostrar el gráfico
fig = px.scatter(filtered_data, x="current_velocity", y="hydrodynamic_force", 
                 size="solidity", color="twine_diameter", 
                 labels={
                     "current_velocity": "Velocidad de la corriente (m/s)",
                     "hydrodynamic_force": "Fuerza hidrodinámica (N)",
                     "solidity": "Solidez",
                     "twine_diameter": "Diámetro del hilo (mm)"
                 },
                 title=f"Fuerza hidrodinámica vs Velocidad de la corriente (Ángulo de ataque: {angle}° ± {angle_range}°)")

st.plotly_chart(fig)
