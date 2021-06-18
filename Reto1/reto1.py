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
       # de lo contrario se muestra error
      else:
       print('Error')
       #Si la contraseña no es correcta, se muestra error
    else:
      print('Error')
      #Si el usuario no es correcto, se muestra error
else:
  print('Error')
