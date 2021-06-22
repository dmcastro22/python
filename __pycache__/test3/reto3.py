import os
def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')

def cambiar_contrasena(contrasenavieja):
  contrasenaactual = 0
  contrasenanueva = 0
  confirmenueva = 0
  contrasenaactual=int(input('Ingrese contraseña actual: '))
  if contrasenaactual != contrasenavieja:
    limpiar()
    print('Error')
  elif contrasenaactual == contrasenavieja:
    contrasenanueva=int(input('Ingrese contraseña nueva:'))
    confirmenueva=int(input('Confirme contraseña nueva:'))
    if contrasenanueva == confirmenueva:
      limpiar()
      contrasenaactual=contrasenanueva
      print('Contraseña cambiada con éxito')
    else:
      limpiar()
      print('Error')
  else:
     limpiar()
     print('Error')
     
  return contrasenaactual
def ingresar_coordenadas():
    coordenadas = {'Trabajo':[0,0],
                  'Casa':[0,0],
                  'Parque':[0,0]}
    esexitoso= False
    try: 
        for key in coordenadas:
            latitud = 0
            longitud = 0
            latitud=float(input('Ingrese latitud: '))
            if latitud >= 2.548 and latitud <= 2.766:
                longitud=float(input('Ingrese longitud: '))
                if longitud >= -76.879 and longitud <= -76.493:
                    coordenadas[key] = [latitud,longitud] 
                    esexitoso=True
                else:
                    print('Error coordenada')
                    break
            else:
                print('Error coordenada')
                break
    except:
        print('Error')
    return esexitoso


contadorveces = 0
opcion= 0
menu = {'1':'Cambiar contraseña',
        '2':'Ingresar coordenadas actuales',
        '3':'Ubicar zona Wifi más cercana',
        '4':'Guardar archivo con ubicación cercana',
        '5':'Actualizar registros de zonas wifi desde archivo',
        '6':'Elegir opcion de menu favorita',
        '7':'Cerrar sesión'}
menuActualizado = {}

#Se muestra mensaje de bienvenida
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Se muestra mensaje para el ingreso del usuario
nombreusuario= input('Ingrese nombre de usuario: ')
if nombreusuario == "51647":
    #Si el numero de usuario es correcto, se muestra mensaje para el ingreso de la contraseña
    contrasena= input('Ingrese contraseña: ')
    if contrasena == "74615":
        #Si la contraseña es correcta, se muestra el captcha de seguridad
      print("Captcha de Seguridad")
      captcha= input('Ingrese el resultado correcto a la siguiente operación: 647+4= ')
      termino1 = 647
      penultimo= (5+7)-6-1-1
      if (termino1 + penultimo) == int(captcha):
          #Si el captcha ingresado es correcto, se muestra mensaje de sesión iniciada
        print('Sesión Iniciada con éxito')
        while opcion != 7:
         for key in menu:
          print (key, ":", menu[key])
         opcion= int(input("Elija una opción: ")) 
         #Se da la opción
         if opcion == 1:
           contrasena=cambiar_contrasena(contrasena)
         elif opcion == 2:
           fueexitoso=ingresar_coordenadas()
            if fueexitoso== False:
              break 
         elif opcion == 6:
          print("Seleccione opción favorita: ")
          fav= int(input("Seleccione una opción del 1 al 5: ")) #El cliente debe ingresar un numero del 1 al 5
          if fav > 0 and fav <= 5:
             adiv1 = int(input('Las estaciones del año y también los elementos y los puntos cardinales, ese número represento:'))
             #si el cliente ingresa, pasa al captcha. Adivinanza 1
             if adiv1 == 4:
               adiv2= int(input('Si quieres saber quién soy, esperen a que llueva. Contando los colores del arcoíris tendrán la prueba:'))
               #Si acierta, pasa a la adivinanza 2
               if adiv2 == 7:
                print('Elija una opción: ') #Si adivinanza 2 es correcta, se pregunta la opcion del menu favorita 
                menuActualizado['1'] = menu[str(fav)]
                posicion = 2
                for key in menu:
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
            print('Hasta pronto')     
      else:
       print('Error')
       #Si la contraseña no es correcta, se muestra error
    else:
      print('Error')
      #Si el usuario no es correcto, se muestra error
else:
  print('Error')
