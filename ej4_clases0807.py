#CREAR UNA FUNCION PARA CALCULAR EL VALOR MAYOR DE UN ARREGLO

def precioMayor(valores):
    mayor = 0.0
    for x in range(len(valores)):
        if valores[x] > mayor:
            mayor = valores[x]
    return mayor

def nombreMayor(nombres, valores):
    nomMayor = ""
    mayor = 0.0
    for x in range(len(valores)):
        if valores[x] > mayor:
            nomMayor = nombres[x]
    return nomMayor


productos = ["PAN", "ACEITE", "CAVIAR", "FIDEOS", "ATUN", "CARNE"]
precios = [1100, 1300, 15000, 500, 1400, 8000]

print("El Producto con mas Valor es: ", nombreMayor(productos, precios))
print("El Valor del Producto Mayor es: ", precioMayor(precios))