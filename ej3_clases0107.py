#EJEMPLO DE FUNCIONES 1

def suma(n1, n2):
    r = n1 + n2
    return r

def resta(n1, n2):
    r = n1 - n2
    return r

def multiplicacion(n1, n2):
    r = n1 * n2
    return r

def division(n1, n2):
    if n2 != 0:
        r = n1 / n2
    else:
        r = None
    return r

num1 = int(input("Ingrese 1º Numero: "))
num2 = int(input("Ingrese 2º Numero: "))
print("La Division es: ", division(num1, num2))
