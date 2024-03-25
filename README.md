# image-dehazing

The method is from **_Effective Single Image Dehazing by Fusion_** by _Codruta Orniana Ancuti_, _Cosmin Ancuti_ and _Philippe Bekaert_.

## To group members


- I write something helpful to presentation and report in [quantitative_comparison](quantitative_comparison.docx).
- [sots](sots) is downloaded from [Kaggle](https://www.kaggle.com/datasets/balraj98/synthetic-objective-testing-set-sots-reside).
- [sots_oudoor](sots_outdoor) is the output of our adapted method.

## Pre-requisites


- Package requirements:
  - `matplotlib`
  - `numpy`
  - `opencv-python`
  - `scikit-image`




## Usage

- Once the pre-requisites are satisfied, the [inference](inference.py) can be run by running the following command, it produces dehazed images:

  ```bash
  python inference.py
  ```
- [cal_metrics](cal_metrics.py) calculates PSNR and SSIM:

  ```bash
  python cal_metrics.py
  ```

