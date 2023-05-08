
from admin.adminController import menuAdmin
from bodeguero.bodegueroController import menuBodeguero
import main
from iniciarSesion.iniciarSesionModel import consultarCuenta, consultarIdCuenta, consultarIdCuentaBodeguero, consultarIdCuentaMedico, consultarIdLugarMedico, set_app_user_session
from medico.medicoController import menuMedico

def menuIniciarSesion():
    
    print('''
        \n
        ===============================
        |      Menú Inicio Sesion     |
        |-----------------------------|
        |   Si desea regresar,        |
        |   escriba 'x' y presione    |
        |   Enter.                    |
        |                             |
        ===============================
        ''')
    
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if usuario == "x" or contrasena == "x":
        main.menuPrincipal()
        
    elif consultarCuenta(usuario, contrasena) != None:
        
        if consultarCuenta(usuario, contrasena) == "0":
            idUsuario = consultarIdCuenta(usuario, contrasena)
            set_app_user_session(usuario)
            menuAdmin()
            
        elif consultarCuenta(usuario, contrasena) == "1":
        
            idMedico = consultarIdCuentaMedico(usuario, contrasena)
            idUsuario = consultarIdCuenta(usuario, contrasena)
            set_app_user_session(usuario)            
            menuMedico(idMedico)
            

        elif consultarCuenta(usuario, contrasena) == "2":
            idUsuario = consultarIdCuenta(usuario, contrasena)
            
            idBodeguero= consultarIdCuentaBodeguero(usuario, contrasena)
            idLugarMedico = consultarIdLugarMedico(idUsuario)
            print(idLugarMedico)
            menuBodeguero(idBodeguero,idLugarMedico)

    else:
        print("Usuario o contraseña incorrectos")
        print("Intente nuevamente")
        menuIniciarSesion()
        