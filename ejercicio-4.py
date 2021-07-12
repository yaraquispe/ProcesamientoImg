
import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('contr2.jpg')

#realizamos el histograma de la imagen original 
hist = cv2.calcHist([imagen], [0], None, [256], [0, 256])

plt.plot(hist, color = 'blue')
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()

imagen_original = cv2.imread('contr2.jpg')
resultado = cv2.imread('contr2.jpg')

# Convertir las imágenes del formato BGR a RGB porque matplotlib acepta 
# imagenes en formato RGB 
imagen_original = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)


#Detallamos los valores de las variables de Contrast stretching 
a = 0   # límite inferior
b = 255 # límite superior
c = np.min(imagen_original)  # El menor valor de los pixeles
d = np.max(imagen_original)  # El mayor valor de los pixeles


h, w, canales = imagen_original.shape 

def point_operator(pixel_RGB):
    return (pixel_RGB - c) * ((b - a) / (d - c) + a)

for x in range(h):
    for y in range(w):
        resultado[x][y] = point_operator(imagen_original[x][y])
        
        
        
# Mostrar la imágen luego de aplicar el algoritmo 
# del mapeo lineal punto a punto
=plt.imshow(resultado)

#Guardamos la imagen
plt.savefig("resultado.jpg", bbox_inches='tight')