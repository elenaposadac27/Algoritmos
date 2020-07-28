matriz = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13]]

print(matriz[2][1])
print(len(matriz))
print(len(matriz[1]))
print("METODO 1")
for i in range (len(matriz)):
  print ("se muestra los elemento de la lista ", i)
  for j in range (len(matriz[i])):
    print(matriz[i][j])

print("METODO 2")
for lista in matriz:
  print(lista)
  for elemento in lista:
    print(elemento)

lista  =  [2,3,45,234,34,34,34,355,64,654,67587,9]
print(lista[2:6])
print(lista[2:-2])
print(lista[7:9])
print(lista[:])
print(matriz[1][2:4])
lista.sort(reverse=True)
print(lista)
#Se toma como si fuera intervalo cerrado al inicio y abierto al final
