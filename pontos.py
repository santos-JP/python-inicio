import math
x1 = int(input("digite um número: "))
y1 = int(input("digite um número: "))
x2 = int(input("digite um número: "))
y2 = int(input("digite um número: "))

coordenada = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

raiz = math.sqrt(coordenada)
if raiz >= 10:
   print("longe")
else:
   print("perto")