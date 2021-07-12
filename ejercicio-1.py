import matplotlib.pyplot as plt
import cv2
import numpy as np

 
def celulas_muertas(img, imageFile):

	#Obtengo el tamaño de la imagen
    h, w = img.shape

    #IMREAD_GRAYSCALE = Carga la imagen a escala de Grises.
    imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
    for i in range(h):
        for j in range(w):
            if(img[i][j]>=193 and img[i][j]<=195 ):
                imgGray[i][j]=255
            else:
                imgGray[i][j]=0
    cv2.imshow('Sin Celulas Muertas',imgGray)
    
    



imageFile = 'thresh1.png'
image = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Imagen Original',image)
celulas_muertas(image, imageFile)  

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist, color='red' )
plt.xlabel('Intensidad')
plt.ylabel('Pixeles Total')
plt.show()
cv2.destroyAllWindows()
