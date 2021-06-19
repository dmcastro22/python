import os

def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')
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
while opcion != 7:
 for key in menu:
  print (key, ":", menu[key])
 opcion= int(input("Elija una opción: "))
 if opcion == 6:
  print("Seleccione opción favorita: ")
  fav= int(input("Seleccione una opción del 1 al 5: "))
  if fav >= 0 and fav <= 5:
      adiv1 = int(input('Las estaciones del año y también los elementos y los puntos cardinales, ese número represento:'))
      if adiv1 == 4:
        adiv2= int(input('Si quieres saber quién soy, esperen a que llueva. Contando los colores del arcoíris tendrán la prueba:'))
        if adiv2 == 7:
         print('Elija una opción: ')
         menuActualizado['1'] = menu[str(fav)]
         posicion = 2
         for key in menu:
          if(key != str(fav)):
           menuActualizado[str(posicion)] = menu[key]
           posicion+=1
         menu.clear()
         menu = menuActualizado.copy()
         menuActualizado.clear()
         limpiar()
        else:
         print('Error')  
      else:
        print('Error')
      contadorveces += 1
      print(contadorveces)
 elif opcion > 0 and opcion <= 5 :
      print('Usted ha elegido la opcion',(opcion))
      break
 elif opcion == 0 or opcion > 7:
      print('Error')
 elif opcion == 7:     
      print('Hasta pronto')



