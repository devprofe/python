from os import system
def calculoIva(precio):
    r = precio * 0.19
    return r

def calculoTotal(precio, iva):
    r = precio + iva
    return r
    
def raizCubica(numero):
    r = pow(numero,(1/3))
    return r

def opcion1():
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

def opcion2():
    numeros = []
    raices = []

    for x in range(5):
        numeros.insert(x, float(input("Ingrese Numero: ")))
        raices.insert(x, round(raizCubica(numeros[x]),3))

    print("Numeros: ", numeros)
    print("Raices: ", raices)

def opcion3():
    lista = []
    accion = ''
    c = 0
    while accion != 'N':
        lista.insert(c, input("Ingrese dato: "))
        c = c + 1 
        accion = input("Desea Seguir Ingresando? S o N: ")

    print("Los Datos Ingresados son: ", lista)

def sigue():
    system("pause")
    system("cls")

opc = 99
while opc != 0:
    print("MENU")
    print("1 - PRECIOS, IVAS Y TOTALES")
    print("2 - RAIZ CUBICA")
    print("3 - LLENADO CON WHILE E INSERT")
    print("0 - SALIR")
    opc = int(input("Ingrese su Opcion: "))

    if opc == 1:
        opcion1()
        sigue()
    elif opc == 2:
        opcion2()
        sigue()
    elif opc == 3:
        opcion3()
        sigue()
    elif opc > 3 or opc < 0:
        print("USTED DIGITO OPCION INVALIDA")
        sigue()
    elif opc == 0:
        print("ADIOS GRACIAS POR USAR ESTE PROGRAMA")
        exit()