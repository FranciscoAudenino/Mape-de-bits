from PIL import Image


print("ingrese la ruta de la imagen")
USImage_Route = input()

USImage = Image.open(USImage_Route)

USImage.show()

print(f"Nombre de la imagen{USImage.filename}")
print(f"Extension: {USImage.format}")

Img_x, Img_y = USImage.size

print(f"Tamaño: X= {Img_x}, Y= {Img_y}")
print(f"Ruta: {USImage_Route}")