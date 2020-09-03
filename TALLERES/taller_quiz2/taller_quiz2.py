import random  as r
import time

def crear_lista():
    size_list= int (input("ingrese el tamaño de la lista : "))
    lista  = [r.randint(500,2000) for i in range (size_list)]

    return lista

def ordenamiento_burbuja(lista):
    size = len (lista)
    for i in range (size):
        for j in range (0, size-i -1):
            if lista [j]> lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        lista[posicion_actual] = valor_actual
    return lista

def ord_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        izquierda = ord_por_mezcla(izquierda)
        derecha = ord_por_mezcla(derecha)

        i = 0
        j = 0

        k = 0

        while i< len(izquierda) and j < len(derecha): 
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k+= 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        

    return lista

lista = crear_lista()
print(lista)

inicial_burbuja = time.time()
lista_ordenada_burbuja = ordenamiento_burbuja(lista)
final_burbuja = time.time()
print(lista_ordenada_burbuja)
print("Tiempo ordenamianto burbuja:", final_burbuja-inicial_burbuja)


inicial_insercion = time.time()
lista_ordenada_insercion = ordenamiento_por_insercion(lista)
final_insercion = time.time()
print(lista_ordenada_insercion)
print("Tiempo ordenamiento por inserción:", final_insercion-inicial_insercion)

inicial_mezcla = time.time()
lista_ordenada_mezcla = ord_por_mezcla(lista)
final_mezcla = time.time()
print(lista_ordenada_mezcla)
print("Tiempo ordenamiento por mezcla:", final_mezcla-inicial_mezcla)