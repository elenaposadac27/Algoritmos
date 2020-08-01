import time
def imprimir_lista(lista):
  for i in range (len(lista)):
    print(lista[i])

def imprimir_lista_metodo_2(lista):
  for elemento in lista:
    print(elemento)


lista_entrada=[0,1,2,3,4]
incial= time.time()
imprimir_lista(lista_entrada)
final= time.time()
print(final-incial)

incial= time.time()
imprimir_lista_metodo_2(lista_entrada)
final= time.time()
print(final-incial)