from PIL import Image,ImageDraw, ImageFont
import os
def crear_miniatura(ruta):
    imagen = Image.open(ruta)
    imagen.thumbnail((100,100))
    return imagen
carpeta_origen ='imagenes'
carpeta_destino = 'imagenes_miniatura'
os.makedirs(carpeta_destino, exist_ok=True)
for archivo in os.listdir(carpeta_origen):
    if archivo.endswith('.png'):
        ruta_completa = os.path.join(carpeta_origen, archivo)
        imagen_miniatura = crear_miniatura(ruta_completa)
        ruta_guardado = os.path.join(carpeta_destino, archivo)
        imagen_miniatura.save(ruta_guardado)
