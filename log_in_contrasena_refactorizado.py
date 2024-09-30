'''Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta). 
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe 
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la 
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
 Cambia el script para que no distinga entre mayúsculas y minúsculas.'''

from registrar_contrasena import cargar_contrasena

contrasena_registrada = cargar_contrasena()

def comprobar_contrasena(contrasena):

    if contrasena == contrasena_registrada:
        return True
    else:
        print("Contraseña inválida. Inténtelo nuevamente.")
        return False

def pedir_contrasena():
    '''Esta función va a pedir la contraseña al usuario'''
    contrasena = input("Por favor ingrese su contraseña: ")
    
    return contrasena


# Ejemplo de uso

contrasena = pedir_contrasena()

valido = comprobar_contrasena(contrasena)

if valido:
    print("!Bienvenido¡")
elif valido == False:
    contrasena = pedir_contrasena()
    valido = comprobar_contrasena(contrasena)
    if valido:
        print("!Bienvenido¡")
    else:
        print("Error. Contraseña inválida.")
        print("Cerrando programa...")

