import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('contr2.jpg')

#realizmos el histograma de la imagen original 
hist = cv2.calcHist([imagen], [0], None, [256], [0, 256])


Outlier = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)


for i in range(10):
    for j in range(10):
        Outlier[i][j] = 0

cv2.imshow('Outlier',Outlier)
cv2.imwrite('Outlier.jpg',Outlier)

 
img = cv2.imread('Outlier.jpg')
histOut = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histOut, color='blue' )
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()

