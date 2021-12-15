import matplotlib.pyplot as plt
from skimage import data
from skimage import color
from skimage import img_as_float
from img import mydata as my



grayscale_image = img_as_float(my.gorro()[::2, ::2])
image = color.gray2rgb(grayscale_image)

red_multiplier = [1, 0, 1]
yellow_multiplier = [1, 1, 0]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4),
                               sharex=True, sharey=True)
ax1.imshow(red_multiplier * image)
ax2.imshow(yellow_multiplier * image)


plt.show()
