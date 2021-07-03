import os

coordenadas = {'Trabajo':[2,4],    #
               'Casa':[5,6],          #Diccionario
               'Parque':[7,80]}     #

mtx_zona = [['2.698', '-76.680', '63'],
            ['2.724', '-76.693', '20'],
            ['2.606', '-76.742', '680'],
            ['2.698', '-76.690', '15']]

def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')

def calc_distancia(latitud, longitud):
  print (latitud, longitud)
  


def ubicar_zona ():
  global mtx_zona
  global coordenadas
  esexitoso= False
  if coordenadas['Trabajo'] == [0,0] and coordenadas['Casa'] == [0,0] and coordenadas['Parque'] == [0,0]:
    limpiar() 
    esexitoso= True    
    print('Error sin registro de coordenadas')
  else: 
    coordenada_trabajo=coordenadas['Trabajo']
    print('coordenada [latitud, longitud] 1 :', "['",coordenada_trabajo[0],"','",coordenada_trabajo[1],"']")
    coordenada_casa=coordenadas['Casa']
    print('coordenada [latitud, longitud] 2 :', "['",coordenada_casa[0],"','",coordenada_casa[1],"']")
    coordenada_parque=coordenadas['Parque']        
    print('coordenada [latitud, longitud] 3 :', "['",coordenada_parque[0],"','",coordenada_parque[1],"']") 

    ubicacion=float(input('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: '))
    if ubicacion == 1:
      calc_distancia(coordenada_trabajo[0], coordenada_trabajo[1])
    elif ubicacion == 2:
      calc_distancia(coordenada_casa[0], coordenada_casa[1])
    elif ubicacion == 3:
      calc_distancia(coordenada_parque[0], coordenada_parque[1])
    else:
      print('Error ubicación')

ubicar_zona()

  

  









