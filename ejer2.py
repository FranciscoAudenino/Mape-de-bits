from PIL import Image

print("ingrese la ruta de la imagen")
USImage_Route = input()
USImage = Image.open(USImage_Route)


USImage.show()

USImage.save(f"C:/Users/franc/OneDrive/Imágenes/Image_ej2.{USImage.format}")
