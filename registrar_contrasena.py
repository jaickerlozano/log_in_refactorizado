import json

def cargar_contrasena():
    '''Esta función carga la contraseña registrada'''

    with open('contrasena.json', 'r') as file:
        contrasena_registrada = json.load(file)
        return (contrasena_registrada)

def guardar_contrasena(contrasena):
    '''Esta función guarda la contrasena'''

    # abrimos el archivo para guardar la contraseña
    with open('contrasena.json', "w") as file:
        # guardamos la contraseña
        json.dump(contrasena, file)
    
    print("Contraseña registrada exitosamente.")

def registro_de_contrasena():
    '''Esta función pide la contraseña para luego registrarla'''
    
    # pedimos la contraseña que se guardará
    contrasena = input("Ingrese una contraseña para registrarla: ")

    # Llamamos la función donde se guardará la contraseña
    guardar_contrasena(contrasena)

    #return (contrasena)

# Ejemplo de uso

if __name__ == "__main__":
    
    registro_de_contrasena()

    cargar_contrasena()


