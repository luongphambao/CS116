
import matplotlib.image as mplib 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

import cv2 
import cv2
from matplotlib import pyplot as plt
# from sklearn.decomposition import PCA
# image = cv2.imread('dog.12300.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def showImage(image):
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()
img=cv2.imread("dog.12300.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
pca = PCA(20)
converted_data = pca.fit_transform(gray)
converted_data.shape
inv_gray = pca.inverse_transform(converted_data)
inv_gray.shape
showImage(inv_gray)
