import os
import math
import operator

coordenadas = {'Trabajo':[0,0],    #
               'Casa':[0,0],          #Diccionario
               'Parque':[0,0]}     #

dicc_zona = {'zona 1': [2.698,-76.680,63],
            'zona 2': [2.724,-76.693,20],
            'zona 3': [2.606,-76.742,680],
            'zona 4': [2.698,-76.690,15]}

dicc_final = {'actual': ['latitud', 'longitud'],
              'zonawifi1': ['latitud','longitud','usuarios'],
              'recorrido': ['distancia','mediotransporte','tiempopromedio']}

ubicacion=0

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
  esexitoso=False
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
  else:
    principal=float(input('Presione 0 para salir: '))
    if principal == 0:
        esexitoso=True
  return esexitoso 

def cambiar_contrasena(contrasenavieja): #funcion con parametro--> contrasenavieja
  contrasenaactual = 0  #variable
  contrasenanueva = 0    #variable
  confirmenueva = 0      #variable 
  esexitoso = False
  contrasenaactual=int(input('Ingrese contraseña actual:')) #input de la contraseña actual
  if contrasenaactual != contrasenavieja:  #si la contrasena actual es diferente a contrasena vieja entonces
    limpiar()                     #limpia pantalla
    print('Error')       #luego imprime error
  elif contrasenaactual == contrasenavieja:  #si la contrasen actual es igual a la contrasena vieja entonces
    contrasenanueva=int(input('Ingrese contraseña nueva:')) #input contrasena nueva
    confirmenueva=int(input('Confirme contraseña nueva:')) #input confirmacion contrasena nueva
    if contrasenanueva == confirmenueva: # si contrasena nueva es igual a confirme nueva entonces
      limpiar()          #limpia pantalla
      contrasenaactual=contrasenanueva   #la contrasena actual y la contrasena nueva seran iguales
      print('Contraseña cambiada con éxito')  # se imprime este mensaje en pantalla
      esexitoso = True
    else:   #sino
      limpiar()  #limpia pantalla
      print('Error')  #imprime error
  else:  #sino
     limpiar()   #limpia pantalla
     print('Error') #imprime error
     
  return contrasenaactual, esexitoso #me devuelve contrasenaactual de acuerdo al requerimiento estipulado

def ingresar_coordenadas():  #funcion sin parametro

    global coordenadas

    actualizar = ()
    esexitoso= False   #variable ensayo 1
    try: #Inicio de excepvion
        for key in coordenadas: #para key en el diccionario coordenadas
            latitud = 0    #variable latitus
            longitud = 0   #variable longitud
            latitud=float(input('Ingrese latitud: '))  #input para ingresar el valor para latitud
            if latitud >= 2.548 and latitud <= 2.766:  # si latitud es may o = a 2.548 y latitud es men o = a 2.766 entonces
                longitud=float(input('Ingrese longitud: '))  #se ejecuta el input para preguntar por la longitud
                if longitud >= -76.879 and longitud <= -76.493: # si longitud es may o = a -76.879 y longitud es men o = a -76.493 entonces
                    coordenadas[key] = [latitud,longitud]  #que las claves del diccionario coordenadas sean = a los valotes para lat y lon
                else:
                    print('Error coordenada') #si no, imp2.rima error coordenada
                    break
            else:
                print('Error coordenada')  #si no, imprim2.a error coordenada
                break
        coordenada=coordenadas['Trabajo']
        print('coordenada [latitud, longitud] 1 :', "['",coordenada[0],"','",coordenada[1],"']")
        long1=coordenada[1]
        coordenada=coordenadas['Casa']
        print('coordenada [latitud, longitud] 2 :', "['",coordenada[0],"','",coordenada[1],"']")
        long2=coordenada[1]
        coordenada=coordenadas['Parque']        
        print('coordenada [latitud, longitud] 3 :', "['",coordenada[0],"','",coordenada[1],"']")
        long3=coordenada[1]

        if long1 > long2 and long1 > long3:
            print ('El que esta más al oriente es: ', long1)
        if long2 > long1 and long2 > long3:    
            print ('El que esta más al oriente es: ', long2)
        if long3 > long1 and long3 > long2:    
            print ('El que esta más al oriente es: ', long3)
        if long1 < long2 and long1 < long3:
            print ('El que esta más al occidente es: ', long1)
        if long2 < long1 and long2 < long3:    
            print ('El que esta más al occidente es: ', long2)
        if long3 < long1 and long3 < long2:    
            print ('El que esta más al occidente es: ', long3)  

        esexitoso=True
        """ actualizar = float(input('Presione 1,2 o 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menu: '))
        if actualizar >= 1 and actualizar <= 3:
            tipo_coordenada = ''
            if actualizar == 1:
                tipo_coordenada = 'Trabajo'
            if actualizar == 2:
                tipo_coordenada = 'Casa'                
            if actualizar == 3:
                tipo_coordenada = 'Parque'

            latitud = 0    #variable latitus
            longitud = 0   #variable longitud
            latitud=float(input('Ingrese latitud: '))  #input para ingresar el valor para latitud
            if latitud >= 2.548 and latitud <= 2.766:  # si latitud es may o = a 2.548 y latitud es men o = a 2.766 entonces
                longitud=float(input('Ingrese longitud: '))  #se ejecuta el input para preguntar por la longitud
                if longitud >= -76.879 and longitud <= -76.493: # si longitud es may o = a -76.879 y longitud es men o = a -76.493 entonces
                    coordenadas[tipo_coordenada] = [latitud,longitud]  #que las claves del diccionario coordenadas sean = a los valotes para lat y lon
                    esexitoso=True #variable ensayo 2 --> para confirmar si el codigo entr
                    limpiar()
                else:
                    limpiar()
                    print('Error actualización') #si no, imp2.rima error coordenada
            else:
                limpiar()
                print('Error ubicación')  #si no, imprim2.a error coordenada      
        elif actualizar == 0:
            limpiar()
            esexitoso=True
        else:
            limpiar()
            print('Error actualización') """      
    except:
        print('Error')   # la excepcion, si no se cumple el try sería imprimir el mensaje de error en pantalla
    
    return esexitoso

def ubicar_zona ():
  global mtx_zona
  global coordenadas
  global ubicacion
  esexitoso= False
  if coordenadas['Trabajo'] == [0,0] and coordenadas['Casa'] == [0,0] and coordenadas['Parque'] == [0,0]:
    limpiar() 
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
      esexitoso= calc_distancia(*coordenadas['Trabajo']) #acceder al valor de una lista 
    elif ubicacion == 2:
      esexitoso= calc_distancia(coordenada_casa[0], coordenada_casa[1]) #acceder al valor de una lista   
    elif ubicacion == 3:
      esexitoso= calc_distancia(coordenadas['Parque'][0],coordenadas['Parque'][1]) #acceder al valor de una lista
    else:
      limpiar()
      print('Error ubicación')
      esexitoso=False
  return esexitoso

def guardar_archivo():
    global ubicacion
    esexitoso=False
    if coordenadas['Trabajo'] == [0,0] and coordenadas['Casa'] == [0,0] and coordenadas['Parque'] == [0,0] and ubicacion == 0:
     limpiar() 
     print('Error de alistamiento')
    else:
        print(dicc_final)
        confirmacion=float(input('¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal: '))
        if confirmacion == 0:
            limpiar()
            esexitoso=True
        if confirmacion == 1:
            limpiar()          
            print('Exportando archivo')
            esexitoso=False

    return esexitoso
     
  

def actualizar_registros():
    datos=float(input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: '))
    if datos == 0:
        limpiar()
        esexitoso=True



contadorveces = 0 #variable contador veces
opcion= 0         # variable opcion
menu = {'1':'Cambiar contraseña',
        '2':'Ingresar coordenadas actuales',
        '3':'Ubicar zona Wifi más cercana',
        '4':'Guardar archivo con ubicación cercana',                           #diccionario
        '5':'Actualizar registros de zonas wifi desde archivo',
        '6':'Elegir opcion de menu favorita',
        '7':'Cerrar sesión'}
menuActualizado = {}            #diccionario vacia

#Se muestra mensaje de bienvenida
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Se muestra mensaje para el ingreso del usuario
nombreusuario= input('Ingrese nombre de usuario: ')  #input para el ingreso de esta info
if nombreusuario == "51647": # si variable nombreusuario es igual a 51647 entonces
    #Si el numero de usuario es correcto, se muestra mensaje para el ingreso de la contraseña
    contrasena= input('Ingrese contraseña: ')  # se ejecuta input para ingresar la contraseña
    if contrasena == "74615": #si la variabe contrasena es igual a 74615 entonces
        #Si la contraseña es correcta, se muestra el captcha de seguridad
      print("Captcha de Seguridad") # se imprime en pantalla el mensaje captcha de seguridad
      captcha= input('Ingrese el resultado correcto a la siguiente operación: 647+4= ') # en este input se debe colocar la solucion 651
      termino1 = 647    # variable termino2 con valor de 647
      penultimo= (5+7)-6-1-1  #variable penultimo con valor 4
      if (termino1 + penultimo) == int(captcha): #condicion si la suma de las dos variables son igual al captcha ingresado linea 87 entonces
          #Si el captcha ingresado es correcto, se muestra mensaje de sesión iniciada
        print('Sesión Iniciada con éxito') #se imprime en pantalla sesion iniciada con exito
        while opcion != 7: #bucle que mientras la variable definida en linea 67 sea diferente a 7 entonces empiece
         for key in menu:   # para key en el diccionario menu
          print (key, ":", menu[key]) #imprima key:valor segun el diccionario menu
         opcion= int(input("Elija una opción: ")) #aparece en pantalla el mensaje para elegir una opcion del menu
         #Se da la opción
         if opcion == 1:  #si la variable opcion es igual a 1 entonces
           contrasena, fueexitoso =cambiar_contrasena(contrasena)  #que la variable contraseña sea igual a la funcion cambiar contrasena con el parametro contrasena
           if fueexitoso == False: # si la variable fue exitoso es igual a False entonces
             break  # se quiebra el proceso y se para el bucle
         elif opcion == 2: #sino si opcion es igual a 2 entonces
           fueexitoso=ingresar_coordenadas() # que la variable fue exitoso sea igual a la funcion ingresar contrasena sin parametro
           if fueexitoso == False: # si la variable fue exitoso es igual a False entonces
            break  # se quiebra el proceso y se para el bucle
         elif opcion == 3:
           fueexitoso=ubicar_zona()
           if fueexitoso == False:
            break
         elif opcion == 4:
             fueexitoso=guardar_archivo()
             if fueexitoso == False:
                 break
         elif opcion == 5:
             fueexitoso=actualizar_registros()
             if fueexitoso == False:
                 break
         elif opcion == 6: #sino si opcion es igual a 6 entonces
          print("Seleccione opción favorita: ")  #imprima en pantalla selecciones opcion favorita
          fav= int(input("Seleccione una opción del 1 al 5: ")) #El cliente debe ingresar un numero del 1 al 5
          if fav > 0 and fav <= 5: # si variable fav es may a 0 y menor o igual a 5 entonces
             adiv1 = int(input('Las estaciones del año y también los elementos y los puntos cardinales, ese número represento:')) #se pregunta por adivi 1
             #si el cliente ingresa, pasa al captcha. Adivinanza 1
             if adiv1 == 4: #si el valor ingresado en adivi 1 es igual a 4 entonces
               adiv2= int(input('Si quieres saber quién soy, esperen a que llueva. Contando los colores del arcoíris tendrán la prueba:')) #se pregunta por adiv 2
               #Si acierta, pasa a la adivinanza 2
               if adiv2 == 7: # si adivi 2 es igual a 7 entonces
                print('Elija una opción: ') #Se imprime en pantalla elija una opcion
                menuActualizado['1'] = menu[str(fav)] # de la variable menuactualizado en la posicion 2 sea igual a 
                posicion = 2 #variable posicion igual a 2
                for key in menu:  # para key en diccionario menu
                 if(key != str(fav)): 
                  menuActualizado[str(posicion)] = menu[key] #este ciclo posiciona la opción favorita en la N°1
                  posicion+=1
                menu.clear()
                menu = menuActualizado.copy()
                menuActualizado.clear()
                limpiar()
               else:
                print('Error')  
             else:
                print('Error')
          elif fav <= 0 or fav >= 6: # Si el cliente ingresa mal la opción 3 veces, saca error en la ejecución y finaliza el proceso
              limpiar()
              print('Error')
              break         
         elif opcion > 1 and opcion <= 5 : 
             # Esta condición define  si el cliente ha seleccionado una de las opciones del 1 al 5 en el menu principal
             limpiar()
             print('Usted ha elegido la opción',(opcion))
             break
         elif opcion == 0 or opcion > 7:
             contadorveces += 1
             if contadorveces == 3:
              limpiar()
              print('Error')
              break 
         elif opcion == 7:
            limpiar()
            print('Hasta pronto')     
      else:
       print('Error')
       #Si la contraseña no es correcta, se muestra error
    else:
      print('Error')
      #Si el usuario no es correcto, se muestra error
else:
  print('Error')
