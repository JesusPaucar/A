import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

# Función para dibujar la flor
def draw_flower(petal_count):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    ax.axis('off')

    # Dibujar el centro de la flor
    ax.scatter(0, 0, s=100, c='yellow', marker='o')

    # Dibujar los pétalos
    petal_colors = ['#FFD700', '#FFAC33', '#FFD700']
    petal_angles = np.linspace(0, 360, petal_count, endpoint=False)

    for angle in petal_angles:
        x = 0.2 * np.sin(np.deg2rad(angle))
        y = 0.2 * np.cos(np.deg2rad(angle))
        petal = plt.Circle((x, y), 0.15, color=np.random.choice(petal_colors))
        ax.add_patch(petal)

    return fig

# Función para enviar el mensaje de primavera
def enviar_mensaje():
    nombre = st.text_input("Nombre", "Andrea")
    mensaje = f"¡Hola {nombre}!\n\n"
    mensaje += "En esta hermosa temporada de primavera, quiero enviarte esta flor virtual\n como un símbolo de la belleza y la renovación que la primavera trae consigo.\n\n"
    mensaje += "Espero que disfrutes de esta estación llena de colores y alegría. \nSonríe, al igual que la primavera lo hace con el mundo.\n\n"
    mensaje += "Saludos,\n Jesus"

    st.text("Mensaje:")
    st.text(mensaje)

# Crear la aplicación Streamlit
def main():
    st.title("Regalo Primaveral Interactivo")

    # Solicitar al usuario el número de pétalos
    petal_count = st.slider("Número de pétalos:", 7, 12, 8)

    # Generar la flor interactiva
    fig = draw_flower(petal_count)

    # Mostrar la figura interactiva de Matplotlib
    st.pyplot(fig)

    # Enviar el mensaje de primavera
    enviar_mensaje()

if __name__ == "__main__":
    main()
