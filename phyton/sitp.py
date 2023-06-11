personalizada=2500
tarjeta=3000
select=int(input("Su tarjeta es Personalizada Digite 1. si la tarjeta es normal  Digite 2.  \n"))
if select==1:
    valor=int(input("Ingrese el valor de su recarga"))
    preg = int(input("Digite 1 para realizar la recarga. De lo contrario digite 2 \n"))
    if preg== 1:
        if valor < personalizada:
            print("Saldo Insuficiente")
        elif valor >= personalizada:
            personalizada= personalizada-valor
            print(f"Su recarga a sido realizada, su saldo actual es {personalizada} recarga tu tarjeta antes de la proxima subida")  
    elif preg == 2:
        print("Ha cancelado la recarga.")
if select==2:
    valor=int(input("Ingrese el valor de su recarga"))
    preg = int(input("Digite 1 para realizar la recarga. De lo contrario digite 2 \n"))
    if preg== 1:
        if valor < tarjeta:
            print("Saldo Insuficiente")
        elif valor >= tarjeta:
            tarjeta= tarjeta-valor
            print(f"Su recarga a sido realizada, su saldo actual es {tarjeta} recarga tu tarjeta antes de la proxima subida")  
    elif preg == 2:
        print("Ha cancelado la recarga.")

else:
    print("se a finalizado la recarga vuelve pronto")     
    