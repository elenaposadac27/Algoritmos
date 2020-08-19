#Codigo de optimizacion de busqueda de un número detereminado

def busqueda_binaria (lista, comienzo, final,objetivo):
    if comienzo > final :
        return False
    medio = (comienzo + final) //2
    if lista [medio] == objetivo:
        return True
    elif lista[medio]< objetivo:
        return busqueda_binaria (lista,medio+1,final,objetivo)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo)

# // muestra el numero exacto, no decimal

