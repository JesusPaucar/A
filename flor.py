import streamlit as st
from PIL import Image, ImageDraw

def generate_flower_image(flower_size, petal_color, center_color):
    # Crear una imagen en blanco
    img = Image.new("RGB", (flower_size, flower_size), "white")
    draw = ImageDraw.Draw(img)

    # Dibujar el centro de la flor
    center_x = flower_size // 2
    center_y = flower_size // 2
    center_radius = flower_size // 10
    draw.ellipse((center_x - center_radius, center_y - center_radius,
                  center_x + center_radius, center_y + center_radius), fill=center_color)

    # Dibujar los pétalos de la flor
    petal_radius = flower_size // 4
    petal_positions = [(center_x, center_y - petal_radius), (center_x - petal_radius, center_y),
                       (center_x + petal_radius, center_y), (center_x, center_y + petal_radius)]

    for pos in petal_positions:
        draw.ellipse((pos[0] - petal_radius, pos[1] - petal_radius,
                      pos[0] + petal_radius, pos[1] + petal_radius), fill=petal_color)

    return img

def main():
    st.title("Mensaje y Flor para una Chica Especial")

    # Introducción y solicitud del nombre de la chica
    st.write("¡Hola! ¿Quién es la chica especial a la que le quieres enviar un mensaje?")
    nombre_de_la_chica = st.text_input("Nombre de la Chica", "")

    # Área de texto para ingresar el mensaje
    st.write("Escribe tu mensaje para ella:")
    mensaje = st.text_area("Mensaje", "")

    # Configuración de la flor
    st.write("Configura la flor:")
    petal_color = st.color_picker("Color de los pétalos", "#FF69B4")
    center_color = st.color_picker("Color del centro", "#FFD700")
    flower_size = st.slider("Tamaño de la flor", 50, 300, 150)

    # Botón para enviar el mensaje y mostrar la flor
    if st.button("Enviar Mensaje y Mostrar Flor"):
        if nombre_de_la_chica and mensaje:
            st.success(f"Mensaje enviado a {nombre_de_la_chica}:")
            st.write(mensaje)
        else:
            st.warning("Por favor, ingresa el nombre de la chica y el mensaje antes de enviarlo.")

        # Generar y mostrar la imagen de la flor
        flower_image = generate_flower_image(flower_size, petal_color, center_color)
        st.image(flower_image, caption="Flor para una Chica Especial", use_column_width=True, channels="RGB")

if __name__ == "__main__":
    main()
