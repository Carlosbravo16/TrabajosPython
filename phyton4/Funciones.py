#declaracion de un metodo sin parametros
def sumar(n1,n2):
    #cuerpo del metodo
    sumar =n1+n2
    return sumar

#Declaracion metodo con parametro
def restar(n1,n2):
    #cuerpo metodo
    restar=n1-n2
    print(f"La resta entre {n1} y {n2} es {restar} ")

#Declaracion con metodo con valor de retorno
def multiplicar(n1,n2):
    #cuerpo metodo
    multiplicar=n1*n2
    #retorno del dato
    return multiplicar
def sumarp():
    seguir="si"
    suma=0
    while seguir=="si":
        numero=int(input("Digite un numero entero"))
        suma=suma+numero
        seguir=input("para seguir ingrese si de lo contrario no")
    return suma

print("Menu opciones")

num1=int(input("Ingrese el numero 1"))
num2=int(input("Ingrese el numero 2"))
num3=int(input("Ingrese el numero 3"))



op=int(input("Ingrese la opcion segun la operacion a realizar \n 1. Suma 2. Resta 3. Multiplicacion 4. Division  5. Promedio"))

if op==1:
    #Invocar metodo suma
    sumar()

elif op==2:
    #Invocacion con un metodo con parametros 
    restar(num1,num2)

elif op==3:
    #Invocar metodo con retorno
    #multiplicar(num1,num2)
    #directamente en una impresion
    print(f"la multiplicacion entre {num1} y {num2} es {multiplicar(num1,num2)}")

#guardar en una variable para operarlo en otro momento 
    producto=multiplicar(num1,num2)
    if producto<50:
        print("el producto es menor que 50")
    else:
        print("el producto es mayo que 50")
elif op==5:
    #se debe utilizar el metodo suma 
    sumar(num1,num2)#suma de los dos numeos
    promedio=sumar(num1,num2)/2
    

