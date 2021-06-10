#archivo=open('prueba.txt','r')
#for linea in archivo.readlines():
 #   print(linea) 
#print(archivo.name)
#archivo.close()
#if archivo.closed:
 #   print('cerrado')

with open ('prueba.txt','r') as archivo:
 #archivo=open('prueba.txt','r')
 suma = 0
 for linea in archivo.readlines(): 
     lista=linea.split(',')
     subtotal= (int(lista[2]*int(lista[3]))*(1+float(lista[4])/100)
     suma= suma + subtotal
     print('concepto: '+lista[1]+' Subtotal: ',subtotal)
print('Total a pagar: ',suma)
print(archivo.closed)


