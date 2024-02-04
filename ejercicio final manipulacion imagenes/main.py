from PIL import Image, ImageFilter, ImageOps
import os
def es_png(imagen):
    if imagen.mode == 'RGBA':
        imagen = imagen.convert('RGB')
    return imagen   
def cambiar_tamaño(imagen, factor_escala = 0.5):
    imagen = es_png(imagen)
    nuevo_tamaño = (int(imagen.width * factor_escala), int(imagen.height * factor_escala))
    return imagen.resize(nuevo_tamaño)
def convertir_a_jpg(imagen):
    if imagen.mode == 'RGBA':
        imagen = imagen.convert('RGB')    
    return imagen
def recortar(imagen, margen=50):
    imagen = es_png(imagen)
    return imagen.crop((margen, margen, imagen.width - margen, imagen.height - margen))
def rotar(imagen, angulo=90):
    imagen = es_png(imagen)
    return imagen.rotate(angulo)
def aplicar_filtro(imagen, filtro='blanco_negro'):
    if filtro == 'blanco_negro':
        return imagen.convert('L')
    elif filtro == 'sepia':
        sepia = ImageOps.colorize(ImageOps.grayscale(imagen),'#704214','#fff8dc')
        return sepia
    elif filtro =='borroso':
        imagen = es_png(imagen)
        return imagen.filter(ImageFilter.GaussianBlur(5))
    return imagen
def procesar_imagenes(carpeta_origen, carpeta_destino, operacion, **kwargs):
    os.makedirs(carpeta_destino, exist_ok=True)
    for archivo in os.listdir(carpeta_origen):
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            ruta_completa = os.path.join(carpeta_origen, archivo)
            imagen = Image.open(ruta_completa)
            imagen_procesada = operacion(imagen, **kwargs)
            nombre_archivo, _ = os.path.splitext(archivo)
            imagen_procesada.save(os.path.join(carpeta_destino, f'{nombre_archivo}_modificado.jpg'))
def mostrar_menu():
    print('Operaciones disponibles: ')
    print('1. Cambiar tamaño')
    print('2. Convertir a JPG')
    print('3. Recortar')
    print('4. Rotar')
    print('5. Aplicar filtro')
    print('6. Salir')
    opcion = input('Selecciona una opcion: ')
    return opcion
def main():
    carpeta_origen = input("Ingresa nombre carpeta origen: ")
    carpeta_destino = input("Ingresa nombre carpeta destino: ")
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            procesar_imagenes(carpeta_origen, carpeta_destino, cambiar_tamaño)
        elif opcion == '2':
            procesar_imagenes(carpeta_origen, carpeta_destino, convertir_a_jpg)
        elif opcion == '3':
            procesar_imagenes(carpeta_origen, carpeta_destino, recortar)
        elif opcion == '4':
            procesar_imagenes(carpeta_origen, carpeta_destino, rotar)
        elif opcion == '5':
            filtro = input("Elige un filtro (blanco_negro, sepia, borroso): ")
            procesar_imagenes(carpeta_origen, carpeta_destino, aplicar_filtro, filtro=filtro)
        elif opcion == '6':
            print('Saliendo...')
            break
        else:
            print("Opcion no valida, intentalo de nuevo")
if __name__ == "__main__":
    main()