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

def enviar_mensaje():
    nombre = st.text_input("Nombre", "Andrea")
    mensaje = f"¡Hola {nombre}!\n\n"
    mensaje += "En esta hermosa temporada de primavera, quiero enviarte esta flor virtual\n como un símbolo de la belleza y la renovación que la primavera trae consigo.\n\n"
    mensaje += "Espero que disfrutes de esta estación llena de colores y alegría. \nSonríe, al igual que la primavera lo hace con el mundo.\n\n"
    mensaje += "Con cariño,\n Jesus"

    st.text("Mensaje:")
    st.text(mensaje)

def main():
    st.title("Regalo Primaveral Interactivo")
    enviar_mensaje()

    # Configuración de la flor
    st.write("Configura la flor:")
    petal_color = st.color_picker("Color de los pétalos", "#FF69B4")
    center_color = st.color_picker("Color del centro", "#FFD700")
    flower_size = st.slider("Tamaño de la flor", 50, 300, 150)

    # Botón para enviar el mensaje y mostrar la flor
    if st.button("Enviar Mensaje y Mostrar Flor"):

        st.success(f"Mensaje enviado a {nombre}:")
        #st.write(mensaje)

        # Generar y mostrar la imagen de la flor
        flower_image = generate_flower_image(flower_size, petal_color, center_color)
        st.image(flower_image, caption="Flor para una Chica Especial", use_column_width=True, channels="RGB")

if __name__ == "__main__":
    main()
