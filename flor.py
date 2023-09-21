import streamlit as st

def main():
    st.title("Flor Interactiva")

    # Configuración de los colores
    petal_color = st.color_picker("Color de los pétalos", "#FF69B4")
    center_color = st.color_picker("Color del centro", "#FFD700")

    # Configurar el tamaño de la flor
    flower_size = st.slider("Tamaño de la flor", 50, 300, 150)

    # Crear el código SVG de la flor
    svg_code = f"""
    <svg height="{flower_size}" width="{flower_size}" xmlns="http://www.w3.org/2000/svg">
        <!-- Centro de la flor -->
        <circle cx="{flower_size // 2}" cy="{flower_size // 2}" r="{flower_size // 10}" fill="{center_color}" />

        <!-- Pétalos de la flor -->
        <circle cx="{flower_size // 2}" cy="{flower_size // 4}" r="{flower_size // 4}" fill="{petal_color}" />
        <circle cx="{flower_size // 4}" cy="{flower_size // 2}" r="{flower_size // 4}" fill="{petal_color}" />
        <circle cx="{(flower_size // 4) * 3}" cy="{flower_size // 2}" r="{flower_size // 4}" fill="{petal_color}" />
        <circle cx="{flower_size // 2}" cy="{(flower_size // 4) * 3}" r="{flower_size // 4}" fill="{petal_color}" />
    </svg>
    """

    # Mostrar la flor SVG en Streamlit
    st.write(svg_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
