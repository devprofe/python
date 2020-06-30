import math
radio = []
area = []
for x in range(5):
    radio.insert(x,float(input("Ingrese Radio: ")))
    area.insert(x,math.pi*pow(radio[x],2))
print("Los Radios Ingresados son: ", radio)
print("Las Areas Obtenidas son: ",area)