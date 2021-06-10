opcion = 0
salir = True
while salir:
    print('1: crear cliente')
    print('2: buscar un cliente')
    print('3: actualizar cliente')
    print('4: salir')
    opcion = int(input('ingrese un valor entre 1 y 4> '))
    if opcion == 1:
        print('opcion 1')
    elif opcion == 2:
        print('opcion 2')
    elif opcion == 3:
        print('opcion 3')
    elif opcion == 4:
        print('opcion 4')
        salir = false
    else:
        print('opcion invalida, por favor entrar valor entre 1 y 4')