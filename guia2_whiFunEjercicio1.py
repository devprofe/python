def calculoIva(precio):
    r = precio * 0.19
    return r

def calculoTotal(precio, iva):
    r = precio + iva
    return r

precios = []
ivas = []
totales = []
resp = ''
x = 0
while resp != 'N':
    precios.insert(x, int(input("Ingrese Precio: ")))
    ivas.insert(x, calculoIva(precios[x]))
    totales.insert(x, calculoTotal(precios[x], ivas[x]))
    x = x + 1
    resp = input("Desea Continuar? S o N: ")
    
print("Precios: ", precios)
print("IVAS 19: ", ivas)
print("Totales: ", totales)