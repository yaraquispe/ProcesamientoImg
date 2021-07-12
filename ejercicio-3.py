

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargamos la imagen del disco duro
imagen = cv2.imread('thresh3.png')
resultado = cv2.imread('thresh3.png')

height, width, chanels= imagen.shape
limi=200 #limite inicial
limf=230 #limite final

#combierte los colores de la cosecha lo verde en negro
for i in range(height):
    for j in range(width):
        if(imagen[i][j][0]>limi or imagen[i][j][1]>limf or imagen[i][j][2]<limi):        
            resultado[i][j]=0

  

#convertimos la imagen a escala de grises 
imgCopia = cv2.imread('thresh3.png', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Imagen a escala de grises', imgCopia)
cv2.imwrite('grises',imgCopia)

hist = cv2.calcHist([imgCopia], [0], None, [256], [0, 256])
cv2.imshow('Imagen original', imagen)


cv2.imshow('Imagen final',resultado)
cv2.waitKey()
cv2.imwrite('Salida.png',resultado)

plt.plot(hist, color='red' )
plt.xlabel('Intensidad')
plt.ylabel('Cantidad Pixeles')
plt.show()

