#INGRESAR VALORES A UNA LISTA, HASTA QUE EL USUARIO DECIDA LO CONTRARIO.

lista = []
respuesta = ''

while respuesta != 'N':
    lista.append(input("Ingrese dato: "))
    respuesta = input("Desea Continuar Ingresando? S o N: ")
print("Los Datos que Ingrese son: ", lista)
