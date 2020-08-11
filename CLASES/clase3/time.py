import time

tiempo_inicial = time.time()
print("HOLA A TODOS COMO ESTAN?")
tiempo_final = time.time()
print(tiempo_final-tiempo_inicial)


tiempo_inicial = time.time()
acumulador= 0
for i in range (100000):
  acumulador +=1
tiempo_final = time.time()
print(tiempo_final-tiempo_inicial)


x= int (input('ingrese cantidad a acumular : '))
tiempo_inicial = time.time()
acumulador= 0
for i in range (x):
  acumulador +=1
tiempo_final = time.time()
print(tiempo_final-tiempo_inicial)



x= int (input('ingrese cantidad a acumular : '))
tiempo_inicial = time.time()
acumulador= 0

for i in range (x):
  for j in range (x):
   acumulador +=1
tiempo_final = time.time()
print (acumulador)
print(tiempo_final-tiempo_inicial)