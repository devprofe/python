#SECUENCIA DE MENU, CON IF y WHILE
opc = 99
while opc != 0:
    print("MENU")
    print("1 - OPCION 1")
    print("2 - OPCION 2")
    print("3 - OPCION 3")
    print("4 - OPCION 4")
    print("0 - SALIR")
    opc = int(input("Ingrese su Opcion: "))

    if opc == 1:
        print("ESTAS EN LA OPCION UNO")
    elif opc == 2:
        print("ESTAS EN LA OPCION DOS")
    elif opc == 3:
        print("ESTAS EN LA OPCION TRES")
    elif opc == 4:
        print("ESTAS EN LA OPCION CUATRO")
    elif opc > 4 or opc < 0:
        print("USTED DIGITO OPCION INVALIDA")
    elif opc == 0:
        print("ADIOS GRACIAS POR USAR ESTE PROGRAMA")
        exit()
