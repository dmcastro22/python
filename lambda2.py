lista= [10,20,30,40,50,60,70,80,90]
promedio =sum(lista)/len(lista)
filtro= list(filter(lambda numero: numero>promedio,lista))
print(filtro)