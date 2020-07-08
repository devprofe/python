#CREAR UNA FUNCION QUE CUENTE LA CANTIDAD DE ELEMENTOS POSITIVOS O 
#NEGATIVOS DE UN ARREGLO.
def positivos(numeros):
    pos = 0
    for x in range(len(numeros)):
        if numeros[x] > 0:
            pos = pos + 1
    return pos

def negativos(numeros):
    neg = 0
    for x in range(len(numeros)):
        if numeros[x] < 0:
            neg = neg + 1
    return neg

def posneg(numeros):
    pos = 0
    neg = 0
    res = []
    for i in range(len(numeros)):
        if numeros[i] < 0:
            neg = neg + 1
        elif numeros[i] > 0:
            pos = pos + 1
    res.append(neg)
    res.append(pos)
    return res


nums = [-5,-4,-2, 3, 6, -7, -8, 10, -9, -100, -5]

print("El Tamaño del Arreglo es: ", len(nums))
print("La Cantidad de Positivos es: ", positivos(nums))
print("La Cantidad de Negativos es: ", negativos(nums))

print("La Cantidad de Negativos y Positivos son : ", posneg(nums))
print("Los Negativos segun posneg: ", posneg(nums).pop(0))
print("Los Positivos segun posneg: ", posneg(nums).pop(1))