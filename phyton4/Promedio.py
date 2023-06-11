contador = 0
suma = 0
numero = 1
while numero !=0:
    numero = int(input("Digite un numero entero (0 para terminar):"))

    if numero !=0:
       suma +=numero
       contador +=1
if contador ==0:
    print("no dogito ningun numero")
else:
    promedio = suma / contador
    print("el promedio de los {} numeros es igual a {}" .format(contador,promedio))
