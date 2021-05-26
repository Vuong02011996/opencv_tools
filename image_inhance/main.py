from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
from glob import glob
import cv2
import numpy as np


def using_pillow(img, path_image):
    image = Image.open(img)
    # increase contrast
    contrast_enhancer = ImageEnhance.Contrast(image)
    factor = 1.5
    output_contrast = contrast_enhancer.enhance(factor)

    # image brightness enhancer
    brightness_enhancer = ImageEnhance.Brightness(output_contrast)
    factor = 1.5
    output_brightness_contrast = brightness_enhancer.enhance(factor)

    output_brightness_contrast.save(path_image[:-1] + img.split("/")[-1][:-4] + "_out.png")


def autoAdjustments_with_convertScaleAbs(image, path_image):
    img = cv2.imread(image)
    alow = img.min()
    ahigh = img.max()
    amax = 255
    amin = 0

    # calculate alpha, beta
    alpha = ((amax - amin) / (ahigh - alow))
    beta = amin - alow * alpha
    # perform the operation g(x,y)= α * f(x,y)+ β
    new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    cv2.imwrite(path_image[:-1] + image.split("/")[-1][:-4] + "_out.png", new_img)

    return [new_img, alpha, beta]


def autoAdjustments(image, path_image):
    # create new image with the same size and type as the original image
    img = cv2.imread(image)
    new_img = np.zeros(img.shape, img.dtype)

    # calculate stats
    alow = img.min()
    ahigh = img.max()
    amax = 255
    amin = 0

    # access each pixel, and auto adjust
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            a = img[x, y]
            new_img[x, y] = amin + (a - alow) * ((amax - amin) / (ahigh - alow))

    cv2.imwrite(path_image[:-1] + image.split("/")[-1][:-4] + "_out.png", new_img)

    return new_img


if __name__ == '__main__':

    path_image = "/home/vuong/Downloads/dark_images_and_enhancement/origin_image/*"
    list_image = glob(path_image)
    for img in list_image:
        # using_pillow(img, path_image)
        # autoAdjustments_with_convertScaleAbs(img, path_image)
        print(img)
        autoAdjustments(img, path_image)



