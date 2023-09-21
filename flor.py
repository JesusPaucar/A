import streamlit as st

def generate_flower_image(flower_size, petal_color, center_color):
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
    return svg_code

def main():
    st.title("Mensaje y Flor para una Chica Especial")

    # Configuración de la flor
    petal_color = st.color_picker("Color de los pétalos", "#FF69B4", key="petal_color")
    center_color = st.color_picker("Color del centro", "#FFD700", key="center_color")
    flower_size = st.slider("Tamaño de la flor", 50, 300, 150)

    # Generar y mostrar la flor SVG
    flower_svg = generate_flower_image(flower_size, petal_color, center_color)
    st.write(flower_svg, unsafe_allow_html=True)

    # Introducción y solicitud del nombre de la chica
    st.write("¡Hola! ¿Quién es la chica especial a la que le quieres enviar un mensaje?")
    nombre_de_la_chica = st.text_input("Nombre de la Chica", "")

    # Área de texto para ingresar el mensaje
    st.write("Escribe tu mensaje para ella:")
    mensaje = st.text_area("Mensaje", "")

    # Botón para enviar el mensaje
    if st.button("Enviar Mensaje"):
        if nombre_de_la_chica and mensaje:
            st.success(f"Mensaje enviado a {nombre_de_la_chica}:")
            st.write(mensaje)
        else:
            st.warning("Por favor, ingresa el nombre de la chica y el mensaje antes de enviarlo.")

if __name__ == "__main__":
    main()

