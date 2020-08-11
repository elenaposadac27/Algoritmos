import time
import codigos_quiz1

#######PUNTO 2: formula segun cantidad de pasos #######
#5+x^3+yx^2+xy

#####PUNTO 3: optimizacion segun tiempo #####

n= int(input("Ingrese la posicion que desea conocer dentro de la sucesion de Fibonacci: \n"))
inicio = time.time() 
print(codigos_quiz1.caso1(n))
final = time.time()
tiempo_caso1 = final-inicio
print(tiempo_caso1)

inicio = time.time() 
print(codigos_quiz1.caso2(n))
final = time.time()
print(inicio,final)
tiempo_caso2 = final-inicio
print(tiempo_caso2)


if tiempo_caso1>tiempo_caso2:
  print("Es mejor el caso 2")
else: 
  print("Es mejor el caso 1")


