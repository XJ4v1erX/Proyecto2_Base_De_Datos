from crearCuenta.crearCuentaModel import insertarBodeguero, insertarUsuario, insertarMedico
import main

def menuCrearCuenta():
    
    print('''
            \n
            ===============================
            |      Menú Crear cuenta      |
            |-----------------------------|
            |   1. Medico                 |
            |   2. Bodeguero              |
            |   3. Regresar               |
            |                             |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            crearMedico()
        case "2":
            crearBodeguero()
        case "3":
            main.menuPrincipal()
        case _:
            print("Opción no válida")
            menuCrearCuenta()
            

contador = 0

def aumentar_contador():
    global contador
    contador += 1
    return contador

def crearMedico():
    
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección: ")
    telefono = input("Ingrese su teléfono: ")
    numColegiado = input("Ingrese su número colegiado: ")
    idEspecialidad = input("Ingrese su especialidad: ")
    idLugarMedico = input("Ingrese su LLugar Medico en el que trabaja: ")
    Usuario = input("Ingrese su usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    idUsuario = aumentar_contador()
    tipousuario = "1"
    
    if  insertarUsuario(Usuario, Contraseña, tipousuario) and insertarMedico(nombre, direccion, telefono, numColegiado,idUsuario, idEspecialidad, idLugarMedico) == True:
            print("Usuario creado con éxito")
            main.menuPrincipal()
    else:
        print("Error al crear usuario")
        crearMedico()

def crearBodeguero():
        
        nombre = input("Ingrese su nombre: ")
        idLugarMedico = input("Ingrese su LLugar Medico en el que trabaja: ")
        Usuario = input("Ingrese su usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
        idUsuario = aumentar_contador()
        print(idUsuario)
        tipousuario = "2"
        
        if insertarUsuario(Usuario, Contraseña, tipousuario) and insertarBodeguero(nombre,idUsuario, idLugarMedico)  == True:
                print("Usuario creado con éxito")
                main.menuPrincipal()
        else:
            print("Error al crear usuario")
            crearBodeguero()
