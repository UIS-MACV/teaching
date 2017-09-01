#PYTHON CON OPENCV

#Se debe importar "cv2"
#Dependencias/Requisitos: opencv previamente instalado
import cv2

#**OPCIONAL**: numpy (libreria para simplificar calculos numericos)
#import numpy as np

#Abrir una imagen
#Parametros: imread("ruta/de/la/imagen.extension", modo)
#modo: es un entero que toma valores de la siguiente forma
#0 --> grayscale (escala de grises, 0 a 255)
#1 --> imagen RGB (a color, contiene valores en los tres canales)
mi_imagen = cv2.imread("kaiju01.jpg",1);

#EJEMPLO 1: a un rango de pixeles
#le aplicaremos color fucsia (B:255, G:0, R:255)
#OJO: en OpenCV las coordenadas son [fila,columna]
for i in range(150,250):
    for j in range(400,580):
        #La imagen es ahora una matriz y puede ser recorrida
        mi_imagen[i,j] = (255,0,255);

#OJO: en OpenCV, el orden de los canales RGB es:
#BLUE GREEN RED (BGR)
#Por lo tanto, (255,0,0) significa: AZUL
cv2.line(mi_imagen,(0,0),(100,200),(255,0,0),5);
cv2.line(mi_imagen,(100,200),(200,50),(0,255,0),5);
cv2.line(mi_imagen,(200,50),(300,150),(0,0,255),5);

#La funcion imshow abre una ventana y en ella
#muestra la imagen que estamos editando
cv2.imshow("titulo ventana",mi_imagen);
cv2.waitKey(0);
cv2.destroyAllWindows();

#Con imwrite guardamos EN DISCO DURO
#los cambios que realizamos
cv2.imwrite("resultado_opencv.png", mi_imagen);


#EJEMPLO 2: abrir un video y almacenar cada uno de sus frames
mivideo = cv2.VideoCapture("video.avi");
success,image = mivideo.read();
conteo = 0;
while success:
    success,image = mivideo.read();
    if success:
        #creamos un nombre de archivo para cada frame
        #Seran almacenados en la carpeta "/frames"
        nuevonombre = "frames/frame"+str(conteo)+".jpg";
        #guardamos el frame actual
        cv2.imwrite(nuevonombre, image);
        conteo += 1
        print "generado frame "+str(conteo);

