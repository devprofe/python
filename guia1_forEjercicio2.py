import math
watts = []
ohms = []
ampers = []
for x in range(7):
    watts.insert(x,float(input("Ingrese Watts: ")))
    ohms.insert(x,float(input("Ingrese Ohms: ")))
    ampers.insert(x,round(math.sqrt(watts[x]/ohms[x]),5))

print("Watts : ", watts)
print("Ohms  : ", ohms)
print("Ampers: ", ampers)