presupuesto = 100000

    
for i in range(1, 6):

    mnj = int(
        input("Escoge una opccion entre el 1 y  el 3 depende de la que desee..?"))
    if mnj == 1:
        resultado = presupuesto - 6000
        print(f"Usted pago su transporte su saldo actual es  {resultado} ")
    elif mnj == 2:
        resultado = presupuesto - 10000
        print(f"Se le gasto onces a la profe su saldo actual es  {resultado} ")
    elif mnj == 3:
        resultado = presupuesto + 5000
        print(
            f"Se trabajo duro y se gano dinero su saldo actual es  {resultado}")
    else:
        print("Es Incorrecta la opcion")

    presupuesto = resultado
