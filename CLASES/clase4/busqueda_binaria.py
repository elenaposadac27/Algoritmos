#Codigo de optimizacion de busqueda de un número detereminado

def busqueda_binaria (lista, comienzo, final,objetivo):
    if comienzo > final :
        return False
    medio = (comienzo + final) //2
    if lista [medio] == objetivo:
        return True
    elif lista[medio]< objetivo:
        return busqueda_binaria (lista,medio+1,final,objetivo)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo)

# // muestra el numero exacto, no decimal

#SE COMENTA DE AQUI PARA ABAJO SOLO PARA PODER REALIZAR EL VERSUS
#Para la busqueda binaria se necesita que la lista esté organizada de menor a mayor, por lo que se utiliza sorted
numero = int (input("ingrese un numero : "))
lista = [9,8,14,2,3,5,22]
lista_ordenada = sorted (lista)
print(lista_ordenada)
encontrado = busqueda_binaria (lista_ordenada,0,len(lista_ordenada),numero)

if encontrado == True :
     print ("El numero existe")
else:
     print ("El numero no existe")
