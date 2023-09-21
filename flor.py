from PIL import Image, ImageDraw
import numpy as np

def draw_flower(petal_count):
    # Tamaño de la imagen y colores
    flower_size = 300
    petal_colors = ['#FFD700', '#FFAC33', '#FFD700']

    # Crear una imagen en blanco
    img = Image.new("RGB", (flower_size, flower_size), "white")
    draw = ImageDraw.Draw(img)

    # Dibujar el centro de la flor
    center_x = flower_size // 2
    center_y = flower_size // 2
    draw.ellipse((center_x - 15, center_y - 15, center_x + 15, center_y + 15), fill='yellow')

    # Dibujar los pétalos
    petal_angles = np.linspace(0, 360, petal_count, endpoint=False)

    for angle in petal_angles:
        x = center_x + 0.2 * flower_size * np.sin(np.deg2rad(angle))
        y = center_y + 0.2 * flower_size * np.cos(np.deg2rad(angle))
        petal = Image.new("RGB", (flower_size, flower_size), "white")
        petal_draw = ImageDraw.Draw(petal)
        petal_draw.ellipse((x - 15, y - 15, x + 15, y + 15), fill=np.random.choice(petal_colors))
        img.paste(petal, (0, 0), petal)

    return img

# Generar una flor con 6 pétalos
flower_image = draw_flower(6)
flower_image.show()
flower_image.save("flower.png")
