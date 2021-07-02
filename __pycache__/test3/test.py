import os

coordenadas = {'Trabajo':[0,0],    #
               'Casa':[0,0],          #Diccionario
               'Parque':[0,0]}     #

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

def ubicar_zona ():
  global mtx_zona
  esexitoso= False
  if coordenadas['Trabajo'] == [0,0] and coordenadas['Casa'] == [0,0] and coordenadas['Parque'] == [0,0]:
    limpiar() 
    esexitoso= True    
    print('Error sin registro de coordenadas')
  
print('coordenada [latitud, longitud] 1 :', [mtx_zona[0][0]], [mtx_zona[0][1]])
print('coordenada [latitud, longitud] 2 :', [mtx_zona[1][0]], [mtx_zona[1][1]])
print('coordenada [latitud, longitud] 3 :', [mtx_zona[2][0]], [mtx_zona[2][1]])
print('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: ')


ubicar_zona()

  

  









