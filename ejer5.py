from PIL import Image
import os, sys

print("ingrese la ruta de la imagen a marcar")
USImage_Route = input()

USImage = Image.open(USImage_Route)

print("ingrese la ruta de la imagen a usar de marca de agua")
MaImage_Route = input()
MAImage = Image.open(MaImage_Route)


print("Ahora eliga donde va a estar la marca de agua:")

print("0 = Superior izquierda")
print("1 = Superior derecha")
print("2 = Inferior izquierda")
print("3 = Inferior derecha")

MaImage_Placement = int(input())

if MaImage_Placement > 3 or MaImage_Placement < 0:
    print("respuesta no valida, reinicie el programa")
    sys.exit

MAImage.resize((25, 25))

USImage_MaxSize_X, USImage_MaxSize_Y = USImage.size
MAImage_MaxSize_X, MAImage_MaxSize_Y = MAImage.size


if MaImage_Placement == 0:
    USImage.paste(MAImage,(50,50))

elif MaImage_Placement == 1:
    USImage.paste(MAImage,((USImage_MaxSize_X-MAImage_MaxSize_X)-50),50)


elif MaImage_Placement == 2:
    USImage.paste(MAImage,(50,(USImage_MaxSize_Y-MAImage_MaxSize_Y)-50))


else:
    USImage.paste(MAImage,((USImage_MaxSize_X-MAImage_MaxSize_X)-50),(USImage_MaxSize_Y-MAImage_MaxSize_Y-50))



Foulder = "Tema3Manipulaion_De_Imagenes\Examen\ejer5_fotos"

if not os.path.exists(Foulder):
    os.makedirs(Foulder)

x = 1

while True:
    File_Route = os.path.join(Foulder, f"Imagen{x}.png")
    
    if not os.path.exists(File_Route):
        break
    x+=1
USImage.save(File_Route)

USImage.show()