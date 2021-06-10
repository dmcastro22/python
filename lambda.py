# def suma(x,y):
#    return x+y 

my_lambda =lambda x,y : x + y #es anonima, no tiene nombre, y se usa para operaciones sencillas (operaciones de una sola linea)
lista= [40,20,54,66,78,90,56] #filtrar los valores mayores que 60
lista2= [4,2,6,7,9,6]
filtro= list(filter (lambda x : x > 60, lista)) #filtro se aplica sobre algunos 
mapa= list(map(lambda x,y : x + y, lista, lista2))  #mapa se aplica sobre todos los de la lista
print (filtro)
print (mapa)

