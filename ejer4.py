from PIL import Image
import os,sys
Cut_Startpoint = []

print("ingrese la ruta de la imagen")
USImagen_Route = input()
USImage = Image.open(USImagen_Route)

Max_Whidth, Max_heigth = USImage.size
print(f"X = {Max_Whidth}, Y = {Max_heigth}")

print("ahora ingrese desde donde quiere empezar a cortar")
Cut_Startpoint.append(int(input("X = ")))
Cut_Startpoint.append(int(input("Y = ")))

while True:
    print("ingrese cuanto de largo quiere cortar")
    Cut_Whidth = int(input())

    print("ingrese cuanto de alto quiere cortar")
    Cut_Heigth = int(input())

    if Cut_Startpoint[0] + Cut_Whidth > Max_Whidth or Cut_Startpoint[0] + Cut_Whidth < 0 or Cut_Startpoint[1] + Cut_Heigth > Max_heigth or Cut_Startpoint[0] + Cut_Heigth < 0 :
        print("ERROR:coordenada no valida, la coordenada ingresada no existe en este archivo; intente resiniciar el programa e insertar una coordenada valida")
        continue
    
    break
Cut_Coords = Cut_Startpoint[0], Cut_Startpoint[1], Cut_Startpoint[0] + Cut_Whidth, Cut_Startpoint[1] + Cut_Heigth
Cut_image = USImage.crop(Cut_Coords)

Foulder = "Tema3Manipulaion_De_Imagenes/Examen/ejer4_recortes"

if not os.path.exists(Foulder):
    os.makedirs(Foulder)

x = 1


while True:
    File_Route = os.path.join(Foulder, f"recorte_{x}.png")
    

    if not os.path.exists(File_Route):
        break
    x+=1
Cut_image.save(File_Route)

Cut_image.show()