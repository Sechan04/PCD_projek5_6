import numpy as np
import imageio as img
import matplotlib.pyplot as plt

image = img.imread('pt.jpeg')

height, width = image.shape[:2]
both_mirror = np.zeros_like(image)

for y in range(height):
    for x in range(width):
        both_mirror[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(both_mirror)
plt.show()