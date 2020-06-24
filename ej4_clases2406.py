#INGRESAR 5 NUMEROS EN UNA LISTA, OBTENER EL NUMERO MAYOR DE LOS 5 INGRESADOS.

numeritos = []
mayor = 0.0
mayor2 = 0.0

for m in range(5):
    numeritos.insert(m, float(input("Ingrese Numeritos: ")))
    if numeritos[m] > mayor:
        mayor = numeritos[m]

mayor2 = max(numeritos)
print("Los numeritos son: ", numeritos)
print("El Mayor de los Numeritos es: ", mayor)
print("El Mayor segun max es: ", mayor2)

