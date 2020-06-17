#DECLARACION DE LISTA CON NOTAS
notas = [2,5.5,2,4,4.5,2,6.5]
suma = 0.0
promedio = 0.0

#MANEJO DE NOTAS MEDIANTE FOR
for x in range(len(notas)):
    suma = suma + notas[x]

#ASIGNACION DE PROMEDIO EN ULTIMA POSICION
promedio = suma/len(notas)
notas.append(promedio)

#CONDICION DE APRUEBA O REPRUEBA
if promedio >= 3.95:
    print("NOTAS DEL ALUMNO: ",notas)
    print("ALUMNO APRUEBA CON : ",promedio)
else:
    print("NOTAS DEL ALUMNO: ",notas)
    print("ALUMNO REPRUEBA CON : ",promedio)
