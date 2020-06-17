#INGRESO DE DATOS
usuario = input("Ingrese Usuario: ")
password = input("Ingrese Contraseña: ")

#CONDICIONES DE PASSWORD
if password.isalnum() and len(password) == 8:
    print("Contraseña VALIDA")
else:
    print("Contraseña INVALIDA")

#QUE HIZO MAL EL USUARIO
if password.isalnum() == False:
    print("USTED INGRESO ESPACIOS EN EL PASS")
elif len(password) != 8:
    print("USTED NO INGRESO 8 CARACTERES")