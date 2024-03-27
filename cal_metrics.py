import os
from skimage.io import imread
from skimage.metrics import structural_similarity
from skimage.metrics import peak_signal_noise_ratio
import glob


def calculate_psnr_ssim(clear_img_names, recon_img_names):
    psnr_list = []
    ssim_list = []

    i = 0
    for clear_img_name, recon_img_name in zip(clear_img_names, recon_img_names):
        clear_img = imread(clear_img_name)
        recon_img = imread(recon_img_name)
        # print(clear_img.shape)
        # print(recon_img.shape)
        # print("clear_img_name: ", clear_img_name, "recon_img_name: ", recon_img_name)

        psnr = peak_signal_noise_ratio(clear_img, recon_img)
        # print(i + 1, clear_img_name, 'PSNR: ', PSNR)
        psnr_list.append(psnr)

        ssim = structural_similarity(clear_img, recon_img, channel_axis=2)
        # print(i + 1, 'SSIM: ', SSIM)
        ssim_list.append(ssim)

        i += 1
    with open('indoor_results.txt', 'a') as f:
        print("Mean PSNR: ", sum(psnr_list) / len(psnr_list), "\nMean SSIM: ", sum(ssim_list) / len(ssim_list), file=f)


clear_img_path = 'sots/indoor/clear'
clear_img_list = []
clear_img_list.extend(sorted(glob.glob(os.path.join(clear_img_path, "*"))))

# print(clear_img_list)
recon_img_path = 'sots_indoor'
recon_img_list = []
recon_img_list.extend(sorted(glob.glob(os.path.join(recon_img_path, "*"))))

# print(recon_img_list)

calculate_psnr_ssim(clear_img_list, recon_img_list)
