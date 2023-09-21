from PIL import Image, ImageDraw
import numpy as np

def draw_flower(petal_count):
    # Tamaño de la imagen y colores
    flower_size = 300
    petal_colors = [(255, 215, 0), (255, 172, 51), (255, 215, 0)]  # Colores en formato RGB

    # Crear una imagen en blanco
    img = Image.new("RGB", (flower_size, flower_size), (255, 255, 255))

    # Crear un objeto para dibujar en la imagen
    draw = ImageDraw.Draw(img)

    # Dibujar el centro de la flor
    center_x = flower_size // 2
    center_y = flower_size // 2
    draw.ellipse((center_x - 15, center_y - 15, center_x + 15, center_y + 15), fill=(255, 255, 0))  # Amarillo

    # Dibujar los pétalos
    petal_angles = np.linspace(0, 360, petal_count, endpoint=False)

    for angle in petal_angles:
        x = center_x + int(0.2 * flower_size * np.sin(np.deg2rad(angle)))
        y = center_y + int(0.2 * flower_size * np.cos(np.deg2rad(angle)))
        draw.ellipse((x - 15, y - 15, x + 15, y + 15), fill=petal_colors[np.random.randint(len(petal_colors))])

    return img

# Generar una flor con 6 pétalos
flower_image = draw_flower(6)

# Mostrar la imagen
flower_image.show()
