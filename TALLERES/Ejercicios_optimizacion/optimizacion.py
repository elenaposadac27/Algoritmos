import time
import codigos

############### caso 1 vs caso 2 #########################
lista =[2,3,4,5,6,2,7]
inicio = time.time() 
codigos.caso1(lista)
final = time.time()
tiempo_caso1 = final-inicio

inicio = time.time() 
codigos.caso2(lista)
final = time.time()
tiempo_caso2 = inicio-final

if tiempo_caso1>tiempo_caso2:
  print("Es mejor el caso 2")
else: 
  print("Es mejor el caso 1")

################### caso 3 vs caso 4 #############################
mensaje = "Hola todo el mundo este mensaje es normal"
inicio = time.time() 
codigos.caso3(mensaje)
final = time.time() 
tiempo_caso3 = inicio-final

inicio = time.time() 
codigos.caso4(mensaje)
final = time.time() 
tiempo_caso4 = inicio-final


if tiempo_caso3>tiempo_caso4:
  print("Es mejor el caso 4")
else: 
  print("Es mejor el caso 3")