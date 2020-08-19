def ord_por_mezcla(lista):
    #caso base
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        #llamada recursiva
        izquierda = ord_por_mezcla(izquierda)
        derecha = ord_por_mezcla(derecha)

        #iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0

        while i< len(izquierda) and j < len(derecha): #mientras podamos seguir comparando
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k+= 1
        #copiar los pedazos de las listas que quedaron
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda  {izquierda}. derecha  {derecha}')
        print(lista)
        print('--' * 30)

    return lista

lista =[1,7,8,3,2,4,9,23,0]
print(ord_por_mezcla(lista))