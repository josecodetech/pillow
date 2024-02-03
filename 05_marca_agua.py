from PIL import Image,ImageDraw, ImageFont
import os
def aplicar_marca(ruta, texto, posicion, font_path='arial.ttf',font_size=30):
    imagen = Image.open(ruta)
    dibujo = ImageDraw.Draw(imagen)
    fuente = ImageFont.truetype(font_path, font_size)
    dibujo.text(posicion, texto, fill=(255,255,255), font= fuente)
    return imagen
carpeta_origen ='imagenes'
carpeta_destino = 'imagenes_marca_agua'
texto_marca_agua ='@josecodetech'
posicion_texto = (10,10)
os.makedirs(carpeta_destino, exist_ok=True)
for archivo in os.listdir(carpeta_origen):
    if archivo.endswith('.png'):
        ruta_completa = os.path.join(carpeta_origen, archivo)
        imagen_marca = aplicar_marca(ruta_completa, texto_marca_agua, posicion_texto)
        ruta_guardado = os.path.join(carpeta_destino, archivo)
        imagen_marca.save(ruta_guardado)
