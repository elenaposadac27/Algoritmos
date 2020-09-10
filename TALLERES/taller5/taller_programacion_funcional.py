#FUNCIONES LAMBDA
#punto 1
elevar = lambda numero = 0, exponente = 0 : numero**exponente
print(elevar(numero=(int(input("Ingrese un valor"))),exponente=(int(input("Ingrese el exponente")))))

#punto2
linea_palabra  = lambda palabra, cantidad = 0: palabra*cantidad
print(linea_palabra(palabra=(input("Ingrese una palabra")),cantidad=(int(input("ingrese la cantidad de veces que desea ver la palabra")))))

#punto3
lista1=[1,16,25,4,2]
lista2=[6,7,32,9,12]

numero_maximo = lambda lista1,lista2 : print(max(lista1), max(lista2))
numero_maximo(lista1,lista2)


#FUNCIONES MAP
#punto1
lista = [3,1,2,3,4]
elevado = lambda elemento :elemento**2
listaCuadrados = list(map(elevado,lista))
print(listaCuadrados)

#FUNCIONES FILTER
#punto1
listica= [3,21,58,63,14,2]
div_7 = lambda elemento : elemento %7 == 0
lista_div_7 = list (filter(div_7,listica))
print (lista_div_7)
