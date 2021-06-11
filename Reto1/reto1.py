print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
nombreusuario= input('Ingrese nombre de usuario: ')
if nombreusuario == "51647":
    contrasena= input('Ingrese contraseña: ')
    if contrasena == "74615":
      print("Captcha de Seguridad")
      captcha= input('Ingrese el resultado correcto a la siguiente operación: 647+4= ')
      termino1 = 647
      penultimo= (5+7)-6-1-1
      if (termino1 + penultimo) == int(captcha):
       print('Sesión Iniciada')
      else:
       print('Error1')
    else:
      print('Error2')
else:
  print('Error3')
