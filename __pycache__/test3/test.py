import os
def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')

def cambiar_contrasena():
  contrasenavieja = 74615
  contrasenaactual = 0
  contrasenanueva = 0
  confirmenueva = 0
  contrasenaactual=int(input('Ingrese contraseña actual: '))
  if contrasenaactual != 74615:
    limpiar()
    print('Error')
  elif contrasenaactual == 74615:
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
        

c=cambiar_contrasena()
print ("tu nueva contra es",c)

  