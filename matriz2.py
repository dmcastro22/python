import math
cont = 0
matrices = dict()
indice = 1
with open('prueba.txt') as archivo:
    for linea in archivo.readlines():
        aux = linea.split(',')
        size_list = len(aux)
        size_mat = int(math.sqrt(size_list))
        lista = list()
        for i in range(size_mat):
            valor=list(map(lambda x: int(x),aux[cont:size_mat]))
            lista.append(valor)
            cont = size_mat 
            size_mat +=size_mat
        cont = 0
        matrices['m'+str(indice)]=lista
        indice +=1
print(matrices)
m1 = matrices['m1']
m2 = matrices['m2']
suma =list()
for i in range(len(m1)):
    aux = list()
    for j in range(len(m2)):
        a = m1[i][j]+m2[i][j]
        aux.append(a)
    suma.append(aux)
print(suma)