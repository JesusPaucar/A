import streamlit as st
import svgwrite

def generate_flower_image(flower_size, petal_color, center_color):
    # Crear un objeto SVG
    dwg = svgwrite.Drawing(size=(flower_size, flower_size))
    
    # Dibujar el centro de la flor
    dwg.add(svgwrite.shapes.Circle(center=(flower_size/2, flower_size/2), r=flower_size/10, fill=center_color))
    
    # Dibujar los pétalos de la flor
    petal_radius = flower_size / 4
    petal_positions = [(flower_size/2, flower_size/4), (flower_size/4, flower_size/2),
                       ((flower_size/4)*3, flower_size/2), (flower_size/2, (flower_size/4)*3)]
    
    for pos in petal_positions:
        dwg.add(svgwrite.shapes.Circle(center=pos, r=petal_radius, fill=petal_color))
    
    # Obtener el código SVG como cadena
    svg_code = dwg.tostring()
    
    return svg_code

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

        # Mostrar la flor SVG
        flower_svg = generate_flower_image(flower_size, petal_color, center_color)
        st.image(flower_svg, caption="Flor para una Chica Especial", use_column_width=True)

if __name__ == "__main__":
    main()
