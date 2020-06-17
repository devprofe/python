#LISTA CON PRECIOS
precios = [100,200,452,478,522,6330,14,251,2557,855]

#LISTA DE PRECIOS INVERTIDA CON TECNICA SLICE
invertida = precios[::-1]

#LISTA QUE GUARDARA RESULTADOS
suma = []

#OPERACION MEDIANTE FOR
for x in range(len(precios)):
    suma.insert(x, precios[x] + invertida[x])

#MUESTRA DE RESULTADOS
print("Precios : ",precios)
print("Invertida: ",invertida)
print("Suma: ",suma)