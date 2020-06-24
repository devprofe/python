#CREAR UNA LISTA DE VALORES (5), ALMACENAR UN IVA PARA CADA VALOR Y UN
#TOTAL A PAGAR POR CADA VALOR, MOSTRAR LISTAS GENERADAS.

valores = []
ivas = []
totales = []

for j in range(5):
    valores.insert(j, float(input("Ingrese Valor: ")))
    ivas.insert(j, valores[j] * 0.19)
    totales.insert(j, valores[j] + ivas[j])

print("Los Valores son: ",valores)
print("El iva 0.19 son: ",ivas)
print("Los Totales son: ",totales)