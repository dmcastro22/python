import os
import math
import operator

coordenadas = {'Trabajo':[2.548,-76.879],    #
               'Casa':[2.550,-76.860],          #Diccionario
               'Parque':[2.553,-76.865]}     #

dicc_zona = {'zona 1': [2.698,-76.680,63],
            'zona 2': [2.724,-76.693,20],
            'zona 3': [2.606,-76.742,680],
            'zona 4': [2.698,-76.690,15]}

def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia*1000

def calc_distancia(latitud, longitud):
  # recibe la ubicacion actual del usuario X
  # compara informacion entre locacion y redes
  diccionario3= {}
  for key in dicc_zona:
    distancia = haversine(latitud, longitud, dicc_zona[key][0], dicc_zona[key][1])        
    diccionario3[dicc_zona[key][2]]=[distancia,dicc_zona[key][0], dicc_zona[key][1]]
    #crear diccionarion con clave usuario y valor distancia X
    #ordenar diccionario por distancia
  sortedDict = sorted(diccionario3.items(), key=operator.itemgetter(1))
  sortedDict.pop(2)
  sortedDict.pop(2)
  sortedDict.sort(key=lambda x: x[0])  
  
  print('Zonas wifi cercanas con menos usuarios')
  print('La zona wifi 1: ubicada en [',sortedDict[0][1][1],sortedDict[0][1][2],'] a',sortedDict[0][1][0],'metros, tiene en promedio',sortedDict[0][0],'usuarios')
  print('La zona wifi 2: ubicada en [',sortedDict[1][1][1],sortedDict[1][1][2],'] a',sortedDict[1][1][0],'metros, tiene en promedio',sortedDict[1][0],'usuarios')

  indicaciones=float(input('Elija 1 o 2 para recibir indicaciones de llegada: '))
  if indicaciones == 1: 
    if latitud < sortedDict[0][1][1]:
      print ('Para llegar a la zona wifi dirigirse primero al norte')
    else:
      print ('Para llegar a la zona wifi dirigirse primero al sur')
    if longitud < sortedDict[0][1][2]:
      print ('y luego hacia el oriente')
    else:
      print ('y luego hacia el occidente')  

    tiempo1pie=(sortedDict[0][1][0]/0.483)
    tiempo1auto=(sortedDict[0][1][0]/20.83)
    print('El tiempo promedio a pie es:',tiempo1pie, 'minutos y el tiempo promedio en auto es:',tiempo1auto,'minutos')

  if indicaciones == 2:
    if latitud < sortedDict[1][1][1]:
      print ('Para llegar a la zona wifi dirigirse primero al norte')
    else:
      print ('Para llegar a la zona wifi dirigirse primero al sur')
    if longitud < sortedDict[1][1][2]:
      print ('y luego hacia el oriente')
    else:
      print ('y luego hacia el occidente')    

    tiempo2pie=(sortedDict[1][1][0]/0.483)
    tiempo2auto=(sortedDict[1][1][0]/20.83)    
    print('El tiempo promedio a pie es:',tiempo2pie, 'minutos y el tiempo promedio en auto es:',tiempo2auto,'minutos')

  if indicaciones != 1 and indicaciones != 2:
    limpiar()
    print('Error zona wifi')

  principal=float(input('Presione 0 para salir: ')) 
 
def ubicar_zona ():
  global mtx_zona
  global coordenadas
  esexitoso= False
  if coordenadas['Trabajo'] == [0,0] and coordenadas['Casa'] == [0,0] and coordenadas['Parque'] == [0,0]:
    limpiar() 
    esexitoso= True    
    print('Error sin registro de coordenadas')
  else: 
    coordenada=coordenadas['Trabajo']
    print('coordenada [latitud, longitud] 1 :', "['",coordenada[0],"','",coordenada[1],"']")
    coordenada_casa=coordenadas['Casa']
    print('coordenada [latitud, longitud] 2 :', "['",coordenada_casa[0],"','",coordenada_casa[1],"']")
    coordenada=coordenadas['Parque']        
    print('coordenada [latitud, longitud] 3 :', "['",coordenada[0],"','",coordenada[1],"']") 

    ubicacion=float(input('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: '))
    if ubicacion == 1:
      calc_distancia(*coordenadas['Trabajo']) #acceder al valor de una lista
    elif ubicacion == 2:
      calc_distancia(coordenada_casa[0], coordenada_casa[1]) #acceder al valor de una lista
    elif ubicacion == 3:
      calc_distancia(coordenadas['Parque'][0],coordenadas['Parque'][1]) #acceder al valor de una lista
    else:
      print('Error ubicación')

ubicar_zona()

  

  









