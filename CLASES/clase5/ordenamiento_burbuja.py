def ordenamiento_burbuja(lista):
    size = len (lista)
    for i in range (size):
        print(lista)
        for j in range (0, size-i -1):
            if lista [j]> lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
                print(lista)
    return lista

lista =[1,3,4,12,2,8,9]
lista_ordenada= ordenamiento_burbuja(lista)
print(lista_ordenada)
