from rembg import remove
from PIL import Image
import os

carpeta = 'imagenes'
nombre_original = 'imagen_con_fondo.jpeg'
ruta_original = os.path.join(carpeta, nombre_original)
nombre_sin_fondo = 'imagen_sin_fondo.png'
ruta_sin_fondo = os.path.join(carpeta, nombre_sin_fondo)

entrada = Image.open(ruta_original)
salida = remove(entrada)
salida.save(ruta_sin_fondo)

imagen = Image.open(ruta_sin_fondo)
imagen.show()
