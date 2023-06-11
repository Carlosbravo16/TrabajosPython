baul = []
op = 1
cont = -1
while (op == 1):
    opcion = int(input("Bienvenidos al baul SENA \n 1. Agregar un articulo al final de la lista\n 2. listar articulos de baul de forma desendenten \n 3. Borrar el ultimo elemento \n 4. borrar un articulo seleccionado dependiendo su posicion \n "))
    if (opcion == 1):
        op2 = 1
        while (op2 == 1):
            agregar = (
                input("Indique el nombre del articulo aguregar a la lista BAUL\n"))
            baul.append(agregar)
            op2 = int(input(
                "Desea agregar otro elemento?\n 1. para continuar \n 2. para terminar de agregar\n"))
    if (opcion == 2):
        print("Su lista quedo de la siguiente manera:\n")
        # for para listas
        for index, i in enumerate(baul):
            print(index, i)
    elif (opcion == 3):
        baul.pop()
        print("Su lista quedo de la siguiente manera:\n", baul)
    elif (opcion == 4):
        print("Su lista esta de la siguiente manera:\n")
        for i in baul:
            cont = cont+1
            print(i, "posicion", cont)
        listar = int(
            input("Indique la posicion del dato que desea eliminar\n"))
        del baul[listar]
        print("Su lista quedo de la siguiente manera:\n", baul)
    else:
        print("Los valores son incorrectos")
    op = int(input(
        "Selcecione \n 1. Para volver en el menu BAUL \n 2. Para salir del programa\n"))
print("Al final su lista quedo de la siguiente manera:\n")
for i in baul:
    cont = cont+1
    print(i, "posicion", cont)
