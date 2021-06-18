import os

menu_print = "¿Qué desea hacer?\n1) Insertar Usuario\n2) Buscar Usuario\n3) Actualizar Usuario\n4) Eliminar Usuario\n5) Mostrar todos\n6) Salir del menú"
#aux = {"cedula": 0, "nombre": "", "apellidos": "", "direccion": ""}
menu = True
def menu(seleccion:int):
    if seleccion ==1:
        insertar()
    elif seleccion==3:
        actualizar()
    elif seleccion ==4:
        borrar()
    else:
        select_all()

def buscar(cedula:str=""):
    contador = 0
    with open('prueba.txt', 'r') as archivo:
        for linea in archivo.readlines():
            aux = linea.split(";")
            if aux[0]==cedula:
                contador +=1
                print(f"Cedula: {aux[0]} | Nombre: {aux[1]} | Apellidos: {aux[2]} | Dirección: {aux[3]}")
            else:
                continue
        if contador ==0:
            print("El usuario que busca no se encuentra registrado")
    return aux
    
def select_all():
    with open('prueba.txt') as archivo: 
        lineas = archivo.readlines()
        for linea in lineas:
            aux = linea.split(";")
            print(f"Cedula: {aux[0]} | Nombre: {aux[1]} | Apellidos: {aux[2]} | Dirección: {aux[3]}")
            
def insertar():
    cedula = input("Ingrese la cédula de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    apellidos = input("Ingrese apellidos de la persona: ")
    direccion = input("Ingrese la direccion de la persona: ")
    with open('prueba.txt','a') as archivo:
        tupla = cedula,nombre,apellidos,direccion
        cadena = ";".join(tupla)
        archivo.write(cadena+"\n")
        print("usuario ingresado con exito")

def actualizar():
    contador = 0
    lineas = []
    cedula = input("Ingrese la cédula de la persona para actualizar: ")
    persona = []
    persona.append(cedula)
    persona2 = buscar(cedula)
    aux = int(input("¿Que valor desea actualizar ?\n1) Nombre\n2) Apellido\n3) Direccion\n4) Todos los anteriores "))
    if aux ==1:
        nombre = input("Ingrese el nombre de la persona: ")
        persona.append(nombre)
        persona.append(persona2[2])
        persona.append(persona2[3]+'\n')
    elif aux ==2:
        apellidos = input("Ingrese apellidos de la persona: ")
        persona.append(persona2[1])
        persona.append(apellidos)
        persona.append(persona2[3]+'\n')

    elif aux==3:
        direccion = input("Ingrese la direccion de la persona: ")
        persona.append(persona2[1])
        persona.append(persona2[2])
        persona.append(direccion+'\n')

    elif aux == 4:
        nombre = input("Ingrese el nombre de la persona: ")
        apellidos = input("Ingrese apellidos de la persona: ")
        direccion = input("Ingrese la direccion de la persona: ")
        persona.append(nombre)
        persona.append(apellidos)
        persona.append(direccion)
    
    with open('prueba.txt','r') as archivo:
        
        for linea in archivo.readlines():
            persona_aux = linea.split(";")
            if persona_aux[0]!=cedula:   
                lineas.append(persona_aux)
            else:
                lineas.append(persona)
       
    with open('prueba.txt','w') as archivo:
        for linea in lineas:
            ingreso = ';'.join(linea)
            #print(type(ingreso))
            archivo.write(ingreso)
   
  
def borrar():
    cedula = input("ingrese la cédula: ")
    contador = 0
    aux = 0
    lineas = []
    with open('prueba.txt','r') as archivo:
        
        for linea in archivo.readlines():
            contador+=1
            persona = linea.split(";")
            if persona[0]!=cedula:   
                lineas.append(persona)
       
    with open('prueba.txt','w') as archivo:
        for linea in lineas:
            ingreso = ';'.join(linea)
            archivo.write(ingreso)

while menu:
    print(menu_print)
    try:
        seleccion = int(input("Ingrese un numero de acuerdo a la acción que desea realizar "))
        os.system('cls')
        if seleccion ==6:
            menu = False
        elif seleccion == 2:
            cedula = input("Ingrese la cedula: ")
            persona = buscar(cedula)
        elif seleccion<1 or seleccion>5:
            raise ValueError("Ingrese un número entre 1 y 4 dependiendo la acción que desea realizar ")
        else: 
            menu(seleccion)
    except ValueError as ve:
        print("Ingrese un valor válido-->"+ve)
    except Exception as ex:
        print(f"Error -> {ex}")