#INGRESAR 3 VALORES A UNA LISTA, ALMACENAR LA RAIZ CUADRADA DE CADA VALOR EN OTRA LISTA

#IMPORTAR LIBRERIA MATEMATICA
import math
num = []
res = []

for r in range(3):
    num.append(int(input("Ingrese Numero: ")))
    res.append(math.sqrt(num[r]))

print("Los Numeros son: ",num)
print("La Raiz de los Numeros son: ",res)
