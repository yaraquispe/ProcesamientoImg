
import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('contr2.jpg')

#realizmos el histograma de la imagen original 
histOriginal = cv2.calcHist([imagen], [0], None, [256], [0, 256])


imagen_original = cv2.imread('contr2.jpg')
resultado = cv2.imread('contr2.jpg')

##################GENERACION DE OUTLIER##################################

Outlier = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)
res = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)


for i in range(10):
    for j in range(10):
        Outlier[i][j] = 0

#cv2.imshow('Outlier',Outlier)


#####################################################################


# Convertir las imágenes del formato BGR a RGB porque matplotlib acepta 
# imagenes en formato RGB 
imagen_original = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)


####################OUTLIER###############################################

#Detallamos los valores de las variables de Contrast stretching 
a = 0   # límite inferior
b = 255 # límite superior
c = np.min(imagen_original)  # El menor valor de los pixeles
d = np.max(imagen_original)  # El mayor valor de los pixeles


#Funcion para crear limites en nuestro rango del histograma 
#para asi  afrontar el outlier
def limite(porcentaje):#Mandamos el porcentaje que queremos reducir
        longi=d-c   #calculamos la longitud del rango
        limite=(longi*porcentaje)/100 #calculamos el limite a partir del porcentaje
        return (int(limite))

newc=c-limite(5)# El menor valor  en un limite de 5% 
newd=d+limite(5)# El menor valor en un limite de 95%



#print("Son: ")

#print(newc,newd)
h, w, canales = imagen_original.shape
#print(c,d)
#print(min,max)


def point_operatorOutlier(pixel_RGB):#Utilizamos operador punto
    return (pixel_RGB - newc) * ((b - a) / (newd - newc) + a)#Remplazamos los nuevos valores de c y d ya reducidos

for x in range(h):
    for y in range(w):
        re = point_operatorOutlier(Outlier[x][y])#aplicamos el operador punto 
        if(re<0):
            res[x][y]=0  
        elif(re>255):
            res[x][y]=255
        else:
            res[x][y]=re
       
hisRes = cv2.calcHist([res], [0], None, [256], [0, 256])
        
cv2.imwrite('limites.jpg',res)#Guardamos la imagen resultante        


plt.plot(histOriginal, color = 'blue')
plt.plot(hisRes, color='green')
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()




