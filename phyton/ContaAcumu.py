presupuesto = 100000
op = 1
opci1 = 0
opci2 = 0
opci3 = 0

while op==1:

    mnj = int(input("Escoge una opccion entre el 1 y  el 3 depende de la que desee..?"))
    if mnj == 1:
        resultado = presupuesto - 6000
        opci1 = opci1 +1
        print(f"Usted pago su transporte su saldo actual es  {resultado} ")
    elif mnj == 2:
        resultado = presupuesto - 10000
        opci2 = opci2 +1
        print(f"Se le gasto onces a la profe su saldo actual es  {resultado} ")
    elif mnj == 3:
        resultado = presupuesto + 5000
        opci3 = opci3 +1
        print(
            f"Se trabajo duro y se gano dinero su saldo actual es  {resultado}")
    else:
        print("Es Incorrecta la opcion")

    presupuesto = resultado

    op=int(input("Digite 1 si desea escoger otra opcion, de lo contrario digite 2 "))

print(f"La cantidad de veces que se repitio cada opcion con la suma de lo que se gasto es: \n opcion 1: {opci1}, {opci1*6000} \n opcion 2:{opci2}, {opci2*10000} \n opcion 3: {opci3}, {opci3*5000}")