celsius = []
kelvin = []
fahrenheit = []
for x in range(1):
    celsius.insert(x, float(input("Ingrese Celsius: ")))
    kelvin.insert(x, celsius[x] + 273.15)
    fahrenheit.insert(x, ((kelvin[x] - 273.15) * 1.8) + 32)
    
print("Celsius: ", celsius)
print("Kelvin: ", kelvin)
print("Fahrenheit: ", fahrenheit)