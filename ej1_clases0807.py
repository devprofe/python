#CREAR UNA FUNCION PARA CALCULAR EL PROMEDIO DE 3 NOTAS.
def promedio3(n1, n2, n3):
    r = (n1 + n2 + n3) / 3
    return r


nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
res = 0.0

nota1 = float(input("Ingrese Nota 1:"))
nota2 = float(input("Ingrese Nota 2:"))
nota3 = float(input("Ingrese Nota 3:"))
res = promedio3(nota1, nota2, nota3)

print("El Promedio es: ", res)