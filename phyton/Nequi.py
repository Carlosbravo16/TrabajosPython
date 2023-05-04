celular = 3144685774
contrasena = 8521
saldo = 4500
op = "s" or "s"
intentos = 3
for i in range(1, 4):
    msj = int(input("ingrese el numero de celular \n"))
    pasword = int(input("Digite los 4 numeros de su contraseña \n"))
    if msj == celular and pasword == contrasena:
        while op == "s" or "s":
            print(f"¡Bienvenido a Nequi..! \n Su saldo es de: {saldo}")
            select = int(input("Digite 1 para sacar dinero. \n Digite 2 para enviar dinero.\n Digite 3 para recargar dinero.\n Digite 4 para hacer un pago  \nDigite 5 para salir de Nequi"))
            if select == 1:
                opcion = int(input("Digite 1 para retirar el dinero por cajero. \n Digite 2 para retirar el dinero en un punto fisico. \n"))
                if opcion == 1:
                    print(f"Su saldo actual es: {saldo}")
                    retiro = int(input("¿Cuanto desea retirar?\n"))
                    if retiro > saldo:
                        print("No tiene fondos para retirar.")
                    elif retiro <= saldo:
                        saldo = saldo - retiro
                        print("Su codigo es: 160692")
                        print(f"Su saldo actual es {saldo}")
                    elif retiro < 2000:
                        print("No te alcanza. ")
                elif opcion == 2:
                    print(f"Su saldo actual es: {saldo}")
                    retiro = int(input("¿Cuanto desea retirar?\n"))
                    if retiro > saldo:
                        print("No tiene fondos para retirar.")
                    elif retiro <= saldo:
                        saldo = saldo - retiro
                        print("Su codigo es: 160692")
                        print(f"Su saldo actual es {saldo}")
                    elif retiro < 2000:
                        print("No te alcanza. ")
            elif select == 2:
                print(f"Su saldo actual es{saldo}")
                numero = int(input("Ingrese el numero de telefono al que desea enviar el dinero.\n"))
                valor = int(input("Ingrese el valor que desea enviar. \n"))
                if valor > saldo:
                    print("No tienes fondos suficientes para enviar.")
                elif valor <= saldo:
                    saldo = saldo - valor
                    print(f"Usted ha enviado {valor} al numero {numero}, le quedo un saldo de {saldo}")
            elif select == 3:
                recarga = int(input("Ingrese el valor que desea recargar.\n"))
                preg = int(input("Digite 1 para realizar la recarga. De lo contrario digite 2 \n"))
                if preg == 1:
                    saldo = saldo + recarga
                    print(f"Su recarga ha sido realizada exitosamente, su saldo actual es {saldo}")
                elif preg == 2:
                    print("Ha cancelado la recarga.")
            elif select == 4:
                opcion = int(input("1. Si desea pagar celular\n 2. Si desea pagar internet"))
                if opcion == 1:
                    print(f"Su saldo actual es {saldo}")
                    numero = int(input("Ingrese el numero al cual desea hacer el pago.\n"))
                    valor = int(input("Ingrese el valor "))
                    if valor > saldo:
                        print("No tienes fondos suficientes para enviar.")
                    elif valor <= saldo:
                        saldo = saldo - valor
                        print(f"Se a efectuado su pago exitosamente al numero {numero}, le quedo un saldo de {saldo}")
                elif opcion == 2:    
                    print(f"Su saldo actual es {saldo}")
                    numero = int(input("Ingrese el numero de la linea "))
                    valor = int(input("Ingrese el valor que desea pagar"))
                    if valor > saldo:
                        print("No tienes fondos suficientes para enviar.")
                    elif valor <= saldo:
                        saldo = saldo - valor
                        print(f"Se a efectuado su pago exitosamente a la linea {numero} de internet, le quedo un saldo de {saldo}")
            elif select == 5:
                    print("¡Gracias por utilizar Nequi..!")
                    break
            
            op = int(input("Seleccione.\n 1. Si desea otra opcion\n 2. Para salir \n"))
        break
    else:
        intentos = intentos - 1
        print(f"¡Upps! Parece que tus datos de acceso no son correctos, Tienes {intentos} intentos mas ")
        if intentos == 0:
            print("Ha agotado todos sus intentos.")

