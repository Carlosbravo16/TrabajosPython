# Construya un programa en Python que realice las siguientes
# operaciones:
# 1 Permita agregar el nombre de un instructor a la lista
# 2 Lista de los instructores que están en la lista
# 3 Modificar un elemento de la lista (seleccionado por el usuario)
# 4 Borrar un elemento de la lista (seleccionado por el usuario)
# 5 Buscar un elemento particular de la lista por su nombre sin importar las mayúsculas o minúsculas.
# 6 Ordenar la lista de instructores de la A-Z

instructores = ["Jonathan Espitia", "jenifer fajardo"]
op = 1
cont = -1
while (op == 1):
    opcion = int(input("Bienvenidos al SENA \nSeleccione una opcion \n 1. Agregar un instructor a la lista\n 2. Listar los instructores que están en la lista \n 3. Modificar un elemento de la lista \n 4. borrar un instructor, dependiendo su posicion \n 5. Buscar un elemento particular de la lista por su nombre sin importar las mayúsculas o minúsculas \n 6. Ordenar la lista de instructores de la A-Z \n "))
    if (opcion == 1):
        op2 = 1
        while (op2 == 1):
            agregar = (
                input("Indique el nombre del instructor que desea agregar a la lista\n"))
            instructores.append(agregar)
            op2 = int(input(
                "¿Desea agregar otro instructor?\n 1. para continuar \n 2. para terminar de agregar\n"))
    if (opcion == 2):
        print("Su lista de instructores quedo de la siguiente manera:\n")
        # for para listas
        for index, i in enumerate(instructores):
            print(index, i)
    elif (opcion == 3):
        print("Su lista de instructores quedo de la siguiente manera:\n")
        # for para listas
        for posicion, dato in enumerate(instructores):
            print("Instructor: ", dato, " Pocision: ", posicion)
        listar = int(
            input("Indique la posicion del instructor que desea editar\n"))
        nuevo = (input("Indique el dato a remplazar\n"))
        del instructores[listar]
        instructores.insert(listar, nuevo)
        print("Su lista de instructores quedo de la siguiente manera:\n", instructores)
    elif (opcion == 4):
        print("Su lista de instructores quedo de la siguiente manera:\n")
        # for para listas
        for posicion, dato in enumerate(instructores):
            print("Instructor: ", dato, " Pocision: ", posicion)
        listar = int(
            input("Indique la posicion del instructor que desea eliminar\n"))
        del instructores[listar]
        print("Su lista de instructores quedo de la siguiente manera:\n", instructores)
    elif (opcion == 5):
        nombre = input("Digite el nombre del instructor que desa buscar\n")

        def buscar_palabra(nombre):
            if nombre.lower():
                print("El instructor ", nombre,
                      " Se encuentra en la posicion", instructores.index(nombre))
                return True
            else:
                return False

    elif (opcion == 6):
        print("Su lista de instructores esta de la siguiente manera:\n")
        instructores.sort()
        print(instructores)
    else:
        print("Los valores son incorrectos")
    op = int(input(
        "Selcecione \n 1. Para volver en el menu BAUL \n 2. Para salir del programa\n"))
print("Al final su lista quedo de la siguiente manera:\n")
for i in instructores:
    cont = cont+1
    print(i, "posicion", cont)
