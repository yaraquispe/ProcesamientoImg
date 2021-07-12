import cv2
import numpy as np
from matplotlib import pyplot as plt



def No_saludables(img):
    h, w = img.shape
    gray = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
    for i in range(h):
        for j in range(w):
            if(img[i][j]<=170):#Le ponemos el valor de 170 guiandonos de nuestro histograma
                gray[i][j]=255
            else:
                gray[i][j]=0
    cv2.imshow('Sin celulas saludables',gray)


img = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Imagen Original', img)
No_saludables(img)

#Generamos un histograma 
hist = cv2.calcHist([img], [0], None, [256], [0, 255])

plt.plot(hist, color='red')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de Pixeles')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
