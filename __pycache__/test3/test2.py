import os
def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')

def ingresar_coordenadas():  #funcion sin parametro
    coordenadas = {'Trabajo':[0,0],    #
                   'Casa':[0,0],          #Diccionario
                   'Parque':[0,0]}     #

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
                    esexitoso=True #variable ensayo 2 --> para confirmar si el codigo entra
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

        actualizar = int(input('Presione 1,2 o 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menu: '))
        if actualizar => 1 and actualizar <= 3:
            tipo_coordenada= ''
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
        elif actualizar == 0:
            esexitoso=True
        else:
            limpiar()
            print('Error actualización')     
 
    except:
        print('Error1')   # la excepcion, si no se cumple el try sería imprimir el mensaje de error en pantalla

    
    return esexitoso

ingresar_coordenadas()





    


   
#2.548, -76.879        + al occidente
#2.766, -76.493        + al oriente
    
