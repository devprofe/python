lista = []
accion = ''
c = 0
while accion != 'N':
    lista.insert(c, input("Ingrese dato: "))
    c = c + 1 
    accion = input("Desea Seguir Ingresando? S o N: ")

print("Los Datos Ingresados son: ", lista)