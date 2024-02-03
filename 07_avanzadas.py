from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import cv2
imagen_original = Image.open("pillow.png")
brillo = ImageEnhance.Brightness(imagen_original)
imagen_cambiada = brillo.enhance(2.0)
imagen_cambiada.save("pillow_brillo.png")
# imagen_cambiada.show()
imagen_desenfocada = imagen_original.filter(ImageFilter.BLUR)
imagen_desenfocada.save("pillow_filtrada.png")
# imagen_desenfocada.show()
def traduccion(ruta_imagen, desp_x, desp_y):
    imagen = Image.open(ruta_imagen)
    imagen_traducida = ImageChops.offset(imagen, desp_x, desp_y)
    imagen_traducida.save("imagen_traducida.png")
def escalar_imagen(ruta_imagen, escala):
    imagen = Image.open(ruta_imagen)
    
    ancho_nuevo = int(imagen.width * escala)
    alto_nuevo = int(imagen.height * escala)
    imagen_escalada = imagen.resize((ancho_nuevo, alto_nuevo))
    imagen_escalada.save("imagen_escalada.png")
    print('Tamaño original: ')
    print(imagen.size)
    print('Tamaño escalado: ')
    print(imagen_escalada.size)
def rotar_imagen(ruta_imagen, angulo):
    imagen = Image.open(ruta_imagen)
    imagen_rotada = imagen.rotate(angulo)
    imagen_rotada.save("imagen_rotada.png")
traduccion("pillow.png", 100, 100)
escalar_imagen("pillow.png", 3)
rotar_imagen("pillow.png", 120)


