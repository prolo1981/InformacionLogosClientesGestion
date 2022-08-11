import os
from PIL import Image
import glob

list = [i for i in glob.glob("*.png")]

if not "test" in os.listdir():
    os.mkdir("test")

print(list)
print("Ancho ", "Alto")
for i in list:
    img = Image.open(i)
    sizes = str(img.size)
    print(sizes)
    # img.show()

    img4 = img.resize((int(img.width / 2), int(img.height / 2)))  # Cambio tamaño de la imagen
    x = (int(img4.width), int(img4.height))  # tupla con los datos
    print(x)  # imprimo datos
    # img4.show()
    img4.save("test\\" + i + "")
    print("hecho")
    os.startfile("test")
