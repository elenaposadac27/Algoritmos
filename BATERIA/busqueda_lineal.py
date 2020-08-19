import random  as r
import time as t

# r.randint permite crear una lista de número apeatorios en este caso entre 1 y 1000000
def crear_lista():
    size_list= int (input("ingrese el tamaño de la lista : "))
    lista  = [r.randint(1,1000000) for i in range (size_list)]

    return lista

def busqueda_lineal(lista, objetivo):
    encontrado = False

    for elemento in lista:
        if elemento == objetivo:
            encontrado = True
            break

    return encontrado
#break hace que se rompa el ciclo cuando se encuentre el numero 

def busqueda_lineal_original(lista, objetivo):
    encontrado = False

    for i in range (len(lista)):
        if lista[i] == objetivo:
            encontrado = True
            break

    return encontrado