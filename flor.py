import cv2
import numpy as np

def draw_flower(petal_count):
    # Tamaño de la imagen y colores
    flower_size = 300
    petal_colors = [(255, 215, 0), (255, 172, 51), (255, 215, 0)]  # Colores en formato BGR

    # Crear una imagen en blanco
    img = np.zeros((flower_size, flower_size, 3), dtype=np.uint8)

    # Dibujar el centro de la flor
    center_x = flower_size // 2
    center_y = flower_size // 2
    cv2.circle(img, (center_x, center_y), 15, (0, 255, 255), -1)  # Color amarillo en formato BGR

    # Dibujar los pétalos
    petal_angles = np.linspace(0, 360, petal_count, endpoint=False)

    for angle in petal_angles:
        x = center_x + int(0.2 * flower_size * np.sin(np.deg2rad(angle)))
        y = center_y + int(0.2 * flower_size * np.cos(np.deg2rad(angle)))
        cv2.circle(img, (x, y), 15, petal_colors[np.random.randint(len(petal_colors))], -1)

    return img

# Generar una flor con 6 pétalos
flower_image = draw_flower(6)

# Guardar la imagen como "flower.png"
cv2.imwrite("flower.png", flower_image)

# Mostrar la imagen
cv2.imshow("Flor", flower_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
