from PIL import Image
imagen = Image.open('pillow.png')
imagen.transpose(Image.FLIP_LEFT_RIGHT).save('pillow_volteada.png')
imagen.rotate(120).save('pillow_rotada.png')
imagen.crop((200,150,550,300)).save('pillow_recortada.png')
imagen_grises = imagen.convert('L')
imagen_grises.save('pillow_grises.png')
from PIL import ImageFilter
imagen_filtrada = imagen.filter(ImageFilter.BLUR)
imagen_filtrada.save('pillow_filtrada.png')