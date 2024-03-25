from image_dehazing.single_image import ImageDehazing
from skimage.io import imread
import glob
import os
from skimage import io
import numpy as np

# Read images
in_dir = 'sots/outdoor/hazy'
img_list = []
img_list.extend(glob.glob(os.path.join(in_dir, "*.jpg")))
print(len(img_list))
output_dir = 'sots_outdoor/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for in_img in img_list:
    # Create instance of ImageDehazing class
    (file_dir, file_name) = os.path.split(in_img)
    in_img = imread(in_img)

    dehazer = ImageDehazing(verbose=False)
    # Initiate dehazing process by call to dehaze method
    dehazed_data = dehazer.dehaze(in_img, pyramid_height=12)
    output_img = dehazed_data['dehazed']
    output_img *= 250.0
    output_img = output_img.astype(np.uint8)

    output_path = output_dir + file_name
    io.imsave(output_path, output_img)
