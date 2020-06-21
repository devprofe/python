valores = [8555,41225,47844,674,544552,75,6,9955,23365]
mayor = 0
for x  in range(len(valores)):
    if valores[x] > mayor:
        mayor = valores[x]
print("El Valor Mayor de la lista es: ", mayor)