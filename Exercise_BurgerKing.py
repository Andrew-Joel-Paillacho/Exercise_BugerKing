
# ANDREW PAILLACHO
# ALGORITMOS Y ESTRUCTURA DE DATOS

print ("\n-------BIENVENIDO AL BURGER KING-------\n")
print ("Por favor, ingrese sus datos para la factura electronica")

print("\n-----------------------\n")
nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su cedula: ")
correo = input("Ingrese su correo: ")

print("\n-----------------------\n")
numero = int(input("Ingrese el numerto de hambuguesas a adquirir: "))
print("\n-----------------------\n")

print("Ingrese una de las siguientes opciones de hamburguesas: ")
print("1) sencilla")
print("2) doble")
print("3) triple")

print("\n-----------------------\n")
tipo = int(input("ingrese la opcion: "))
print("\n-----------------------\n")

if (tipo == 1):
    precio = numero * 1.5

    print("Ingrese su farma de pago: ")
    print("1) targeta de credito")
    print("2) efectivo")
    
    pago = int(input("Ingrese la opcion: "))
    print("\n-----------------------\n")

    if (pago == 1):
        pagofinal = precio * 1.05

        print(f"genial, {nombre} el precio final a pagar es de {pagofinal}")
        print(f"{nombre} su factura se enviara a su correo {correo}")

        print("Muchas gracias por su visita.")
        print("\n-----------------------\n")
    elif (pago == 2):
        pagofinal = precio

        print(f"genial, {nombre} el precio final a pagar es de {pagofinal}")
        print(f"{nombre} su factura se enviara a su correo {correo}")

        print("Muchas gracias por su visita.")
        print("\n-----------------------\n")
    else:
        print("¡¡¡Esta opcion no es valida!!!")
        print("Esta forma de pago no existe.")
        print("\n-----------------------\n")

elif(tipo == 2):
    precio = numero * 2.5

    print("Ingrese su farma de pago: ")
    print("1) targeta de credito")
    print("2) efectivo")
    
    pago = int(input("Ingrese la opcion: "))
    print("\n-----------------------\n")

    if (pago == 1):
        pagofinal = precio * 1.05

        print(f"genial, {nombre} el precio final a pagar es de {pagofinal}")
        print(f"{nombre} su factura se enviara a su correo {correo}")

        print("Muchas gracias por su visita.")
        print("\n-----------------------\n")
    elif (pago == 2):
        pagofinal = precio

        print(f"genial, {nombre} el precio final a pagar es de {pagofinal}")
        print(f"{nombre} su factura se enviara a su correo {correo}")

        print("Muchas gracias por su visita.")
        print("\n-----------------------\n")
    else:
        print("¡¡¡Esta opcion no es valida!!!")
        print("Esta forma de pago no existe.")
        print("\n-----------------------\n")

elif (tipo == 3):
    precio = numero * 3.25

    print("Ingrese su farma de pago: ")
    print("1) targeta de credito")
    print("2) efectivo")
    
    pago = int(input("Ingrese la opcion: "))
    print("\n-----------------------\n")

    if (pago == 1):
        pagofinal = precio * 1.05

        print(f"genial, {nombre} el precio final a pagar es de {pagofinal}")
        print(f"{nombre} su factura se enviara a su correo {correo}")

        print("Muchas gracias por su visita.")
        print("\n-----------------------\n")
    elif (pago == 2):
        pagofinal = precio

        print(f"genial, {nombre} el precio final a pagar es de {pagofinal}")
        print(f"{nombre} su factura se enviara a su correo {correo}")

        print("Muchas gracias por su visita.")
        print("\n-----------------------\n")
    else:
        print("¡¡¡Esta opcion no es valida!!!")
        print("Esta forma de pago no existe.")
        print("\n-----------------------\n")

else:
    print("¡¡¡Esta opcion no es valida!!!")
    print("Este tipo de hamburguesa no existe en el menu.")
    print("\n-----------------------\n")

