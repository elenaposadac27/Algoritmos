#FUNCIONES ANÓNIMAS
#CASO 1
#-----como sabiamos:
def line_design ():
    print("#"*60)
line_design()

#----Funcion anónima
ejemplo = lambda : print("#"*60)
print("ahora usando lambdas")
ejemplo()

#CASO 2 (CON ENTRADA):
def line_design_e(cantidad):
    print("#"*cantidad)
line_design_e(10)

line = lambda cantidad :print("#"*cantidad)
print("con lambda")
line(2)

#CALCULADORA
# =0 son los valores por defecto
sumar = lambda valor1=0, valor2=0 : valor1+valor2
restar =lambda valor1=0, valor2=0 : valor1-valor2
multiplicar = lambda valor1=0, valor2=0 : valor1*valor2
dividir = lambda valor1=0, valor2=0 : valor1/valor2

print(sumar(1,2))
print(restar(4,2))
print(multiplicar(42,48))
print(dividir(10,4))

#Lambda dentro de lambda:
calculadora = lambda operacion, valor1=0, valor2=0 : print(operacion(valor1,valor2))
calculadora(multiplicar, 83,87)
calculadora(sumar, 83,87)
calculadora(restar, 83,87)
calculadora(dividir, 83,87)


##################################################################
#FUNCIONES MAP
#CASO 1
#----como sabiamos:
listaNotas = [3,1.8,2.7,3.4,4]

for i in range(len(listaNotas)):
    listaNotas[i] +=1
print(listaNotas)

#-----Funcion MAP
listaNotas_m = [3,1.8,2.7,3.4,4]
sumar1 =lambda valor: valor+1
adicionar = list(map(sumar1,listaNotas_m))
print(adicionar)


#CASO 2
#---como sabiamos:
listaNotas2 = [3,1,2,3,4]
for i in range(len(listaNotas2)):
    listaNotas2[i] = listaNotas2[i]**2
print(listaNotas2)

#---Funcion MAP
listaNotas2_m = [3,1,2,3,4]
exponente = lambda elemento :elemento**2
listaCuadrados = list(map(exponente,listaNotas2_m))
print(listaCuadrados)

#FILTER
# % significa residuo (estamos diciendo que cuando al dividir por 2 el residuo es 0, el numero es par)
listaNumeros = [1,2,3,45,23,4,8,9,20]

#---como sabiamos
listaPares = []
for numero in listaNumeros:
    if numero % 2 ==0:
        listaPares.append(numero)
print(listaPares)

#---filter
par = lambda elemento : elemento %2== 0
pares = list(filter(par,listaNumeros))
print(pares)

