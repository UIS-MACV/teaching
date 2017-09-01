#PYTHON CON PIL (PILLOW)

#Se debe importar Image (para funciones basicas, abrir, mostrar, editar)
#**OPCIONAL**: Si se desea dibujar sobre la imagen, se debe importar ImageDraw
from PIL import Image, ImageDraw

#Abrir una imagen
#Parametros: Image.open("ruta/de/la/imagen.extension")
mi_imagen = Image.open("kaiju01.jpg");

#Editar los valores de los pixeles de la imagen
#Funcion: (mi_imagen).load() --> (mi_imagen_edicion)
edicion = mi_imagen.load();

#Ahora podemos acceder y modificar los valores de los pixeles

#EJEMPLO 1: a un rango de pixeles
#le aplicaremos color rojo (R:255, G:0, B:0)
#OJO: coordenadas como [columna,fila]
for i in range(400,580):
    for j in range(150,250):
        #La imagen editable ("edicion") es ahora una matriz y puede ser recorrida
        edicion[i,j] = (255,0,255);

#EJEMPLO 2: dibujar lineas sobre la imagen
draw = ImageDraw.Draw(mi_imagen);

draw.line((0, 0, 100, 200), fill=(0,0,255), width=5);
draw.line((100, 200, 200, 50), fill=(0,255,0), width=5);
draw.line((200, 50, 300, 150), fill=(255,0,0), width=5);

#Mostramos la imagen en una ventana
mi_imagen.show();

#Guardar EN DISCO DURO los cambios realizados
#Funcion: (mi_imagen).save("ruta/de/la/imagen.extension", tipo)
#Tipo: alguno de los formatos soportados. "JPEG", "PNG", etc
mi_imagen.save("resultado_pil.png", "PNG");

