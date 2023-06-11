#crear una lista
lista=["malteada", "perro caliente"]
#agregar un elemento a la lista final
lista.append("hamburguesa")
#agregar varios elementos al final
lista.extend(["pollo", "f"])
#agregar un elemento en una posicion indicada
lista.insert(2, "Empanada")
 
#Borrar un elementode la lista
lista.remove("malteada")
#Borrar un elemento en una pocision indicada
del lista[0]
#Borrar el ultimo elemento de la lista
lista.pop()
#Limpiar lista de arreglo
lista.clear()
#Ordenar acendente
lista.sort()
#Ordenar decendentemente
lista.reverse()
lista.sort(reverse=True)
#devolver la posision del elemento
print(lista.index("pollo"))
#for i in lista:
#       print(1)