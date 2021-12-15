import numpy as np
import matplotlib.pyplot as plt
from img import mydata as my
from skimage import color, data, restoration

couple = color.rgb2gray(my.boneco())
from scipy.signal import convolve2d as conv2
psf = np.ones((5, 5)) / 25
couple = conv2(couple, psf, 'same')
couple += 0.1 * couple.std() * np.random.standard_normal(couple.shape)

deconvolved, _ = restoration.unsupervised_wiener(couple, psf)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5),
                       sharex=True, sharey=True)

plt.gray()

ax[0].imshow(couple, vmin=deconvolved.min(), vmax=deconvolved.max())
ax[0].axis('off')
ax[0].set_title('Data')

ax[1].imshow(deconvolved)
ax[1].axis('off')
ax[1].set_title('Self tuned restoration')

fig.tight_layout()

plt.show()
