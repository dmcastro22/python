adiv1 = int(input('Las estaciones del año y también los elementos y los puntos cardinales, ese número represento:'))
if adiv1 == 4:
   adiv2= int(input('Si quieres saber quién soy, esperen a que llueva. Contando los colores del arcoíris tendrán la prueba:'))
   if adiv2 == 7:
     print('Elija una opciòn: ')
   else:
       print('Error2')  
else:
    print('Error1')




   # for mac and linux(here, os.name is 'posix')
 #  if os.name == 'posix':
      # _ = os.system('clear')
 #  else:
      # for windows platfrom
    # _ = os.system('cls')

      menuActualizado['1'] = menu[str(fav)]
      posicion = 2
      for key in menu:
        if(key != str(fav)):
         menuActualizado[str(posicion)] = menu[key]
         posicion+=1
      menu.clear()
      menu = menuActualizado.copy()
      menuActualizado.clear()