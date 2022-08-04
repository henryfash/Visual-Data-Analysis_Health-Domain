import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcol

palette = np.zeros((500, 500, 3))
# define as HSV, devide among hue values and saturation
hue = 0
sat = 0
for i in range(palette.shape[0]):
    if (i % 100 == 0):
        hue += 0.2
    for j in range(palette.shape[1]):
        if (j % 100 == 0):
            sat += 0.2
            if (sat > 1):
                sat = sat % 1
        palette[i, j] = [hue, sat, 1]
rgb = mcol.hsv_to_rgb(palette)
plt.imshow(rgb)
plt.xticks([])
plt.yticks([])
plt.xlabel("file size")
plt.xscale
plt.ylabel("file type")
plt.show()
