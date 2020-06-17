#DECLARACION DE LISTA CON NOTAS
notas = [2,5.5,2,4,4.5,2,6.5]
suma = 0.0

#MANEJO DE NOTAS MEDIANTE FOR
for contenido in notas:
    suma = contenido + suma

#ASIGNACION DE PROMEDIO EN ULTIMA POSICION
notas.append(suma/len(notas))

#CONDICION DE APRUEBA O REPRUEBA
if notas[7] >= 3.95:
    print("ALUMNO APRUEBA CON : ",notas[7])
else:
    print("ALUMNO REPRUEBA CON : ",notas[7])
