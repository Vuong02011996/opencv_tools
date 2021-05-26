from skimage.exposure import is_low_contrast
from glob import glob
import cv2


if __name__ == '__main__':
    path_image = "/home/vuong/Downloads/dark_images_and_enhancement/*"
    list_image = glob(path_image)
    for img in list_image:
        image = cv2.imread(img)
        # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        low_contrast = is_low_contrast(image, 0.46)

        print("image {} contrast {}".format(img, low_contrast))