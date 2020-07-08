#CREAR UNA FUNCION QUE CALCULE EL PROMEDIO DE NOTAS DE UN ARREGLO.
def promedioNotas(arreglo):
    avg = 0.0
    suma = 0.0
    for c in range(len(arreglo)):
        suma = arreglo[c] + suma
    avg = suma / len(arreglo)
    return avg


notas = [5.5, 6.6, 7, 2.5, 4.5, 5.3, 3.4, 5.8, 7, 1.1, 2.3]
res = promedioNotas(notas)
print("El promedio de las notas es: ", round(res,2))