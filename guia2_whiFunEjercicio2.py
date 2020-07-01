def raizCubica(numero):
    r = pow(numero,(1/3))
    return r

numeros = []
raices = []

for x in range(5):
    numeros.insert(x, float(input("Ingrese Numero: ")))
    raices.insert(x, round(raizCubica(numeros[x]),3))

print("Numeros: ", numeros)
print("Raices: ", raices)