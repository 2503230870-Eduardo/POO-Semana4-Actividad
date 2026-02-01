def menu():
    print("------Menu-----")
    print("1. Saludar")
    print("2. Salir")
    opcion = input("Selecciones una opcion: ")
    return opcion

while True:
    opcion = menu()
    if opcion == "1":
        print("!Hola! Bienvenido a PyCharm.")
    elif opcion == "2":
        break

    else:
        print("Opcion invalida.")