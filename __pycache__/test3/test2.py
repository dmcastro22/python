import os
def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')

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
    print(coordenadas)
    return esexitoso

    
    
x=ingresar_coordenadas()
print(x)
   

       
    

