from PIL import Image

print("ingrese la ruta de la imagen")
USImage_Route = input()
USImage = Image.open(USImage_Route)

print("Ingrese los grados de rotacion que desea aplicar")
Rotate_Amount = int(input())

USImage_Rotated = USImage.rotate(Rotate_Amount)

USImage_Rotated.show()

USImage_Rotated.save(f"C:/Users/franc/OneDrive/Imágenes/nombreArchivoOriginalRot.{USImage.format}")


#“nombreArchivoOriginalRot.ext”