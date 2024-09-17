import cv2
import numpy as np
import timeit

image = cv2.imread("maspcomruido.jpg", 0)
if image is None:
    print("Error: Image not loaded correctly.")
else:
    print(f"Loaded image shape: {image.shape}")

# Filtro media 3x3
def filtro(imagem):
    return cv2.blur(imagem, (3, 3))

# Usar timeit para medir o tempo de execução
def run_filter():
    filtered_image = filtro(image)

total_time_sequential = timeit.timeit(run_filter, number=1)
print(f"Sequential filtering time: {total_time_sequential} seconds")

# Mostrar a imagem filtrada
filtered_image = filtro(image)
cv2.imshow("original image", image)
cv2.imshow("filtered image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
