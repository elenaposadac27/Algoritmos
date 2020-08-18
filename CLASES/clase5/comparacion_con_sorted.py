import busqueda_lineal
import busqueda_binaria
import time
lista = busqueda_lineal.crear_lista()
print(lista)

inicio= time.time()
print (8 in lista)
final_nativo= time.time()-inicio
lista_ordenada = sorted(lista)
inicio= time.time()
print (busqueda_binaria.busqueda_binaria(lista_ordenada,0 , len(lista),8))
final_binario= time.time()-inicio
print (final_nativo)
print(final_binario)