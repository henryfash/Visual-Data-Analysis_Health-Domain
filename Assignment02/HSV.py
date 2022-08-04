import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcol

# read the image
image_rgb = plt.imread("oldtimer.png")
# convert it to hsv
image_hsv = mcol.rgb_to_hsv(image_rgb)
# retain only value channel
image_grayscale = image_hsv[:, :, 2] * 255
plt.imshow(image_grayscale, cmap='gray', vmin=0, vmax=255)
plt.show()
# convert to grayscale by averaging over all rgb channels instead
image_grayscale_alternative = np.sum(image_rgb[:, :, 2]) // 3
# reduce saturation by 50% and display it
image_hsv[:, :, 1] = image_hsv[:, :, 1] * 0.5
image_rgb_reduced_saturation = mcol.hsv_to_rgb(image_hsv)
plt.imshow(image_rgb_reduced_saturation)
plt.show()
# Add some brown
image_brown = np.zeros(image_rgb.shape)
image_brown[:, :] = np.divide([222, 184, 135], 255)
image_rgb_aged = np.copy(image_rgb)
for i in range(image_rgb.shape[0]):
    for j in range(image_rgb.shape[1]):
        image_rgb_aged[i, j] = ((0.5) * image_rgb_aged[i, j] + 0.5 * image_brown[i, j])
plt.imshow(image_rgb_aged)
plt.show()
# rotate image hue to blue
image_hsv_blue = mcol.rgb_to_hsv(plt.imread("oldtimer.png"))
image_hsv_blue[:, :, 0] = (image_hsv_blue[:, :, 0] + 240 / 360) % 1
plt.imshow(mcol.hsv_to_rgb(image_hsv_blue))
plt.show()
# rotate image hue to yellow
image_hsv_yellow = mcol.rgb_to_hsv(plt.imread("oldtimer.png"))
image_hsv_yellow[:, :, 0] = (image_hsv_yellow[:, :, 0] + 60 / 360) % 1
plt.imshow(mcol.hsv_to_rgb(image_hsv_yellow))
plt.show()
