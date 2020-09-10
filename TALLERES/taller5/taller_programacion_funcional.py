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

#punto2
dividir = lambda elemento : elemento/max(lista)
listaCocientes = list(map(dividir,lista))
print(listaCocientes)

#punto3
numero = int(input("ingrese el valor que desea restar"))
restar = lambda elemento : elemento - numero
listaDiferencias= list(map(restar,lista))
print(listaDiferencias)

#FUNCIONES FILTER
#punto1
listica= [3,21,58,63,14,2]
div_7 = lambda elemento : elemento %7 == 0
lista_div_7 = list (filter(div_7,listica))
print (lista_div_7)

#punto2
listaEstudiantes=["Juan", "Sofia", "Nicolas", "Sebastian", "Maria Clara", "Ana"]
largoMenor5 = lambda nombre : len(nombre) < 5
lista_nombres_menores_5 = list(filter(largoMenor5,listaEstudiantes))
print(lista_nombres_menores_5)

#punto3
Numeros=[5,2,8,20,6,10,53,85,32,14,9]
par = lambda elemento : elemento %2 == 0
listaPares = list (filter(par,Numeros))
print (listaPares)

#punto4
impar = lambda elemento : elemento %2 != 0
listaImpares = list (filter(impar,Numeros))
print (listaImpares)

#FUNCIONES REDUCE
from functools  import reduce
#punto1
listaRed = [10,9,8,7,6,5,4,3,2]
sumatoria_restas = lambda acumulador =0 , elemento =0 : acumulador - elemento
resultado = reduce (sumatoria_restas, lista)
print (resultado)

#punto2
palabras = ["El ","carro ", "es ", "blanco"]
frase = lambda acumulador =0 , elemento =0 : acumulador + elemento
fraseResultante = reduce (frase, palabras)
print (fraseResultante)

#punto3
numerosEnteros = [5,3,6,8,4,7,2]
dividir = lambda elemento : elemento/2
resultado = list(map (dividir,numerosEnteros))

sumatoria = lambda acumulador =0 , elemento =0 : acumulador + elemento
listaResultante = list(reduce (sumatoria, resultado))
print (listaResultante)

#preguntar por este ultimo punto