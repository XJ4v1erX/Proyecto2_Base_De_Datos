
from configuracion.config import connect
import iniciarSesion.iniciarSesionController 
import crearCuenta.crearCuentaController 

def menuPrincipal():
    
    print('''
            \n
            ===============================
            |         Menú principal      |
            |-----------------------------|
            |   1. Iniciar Sesion         |
            |   2. Crear Cuenta           |
            |   3. Salir                  |
            |                             |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            iniciarSesion.iniciarSesionController.menuIniciarSesion()
        case "2":
            crearCuenta.crearCuentaController.menuCrearCuenta()
        case "3":
            print("Hasta luego")
        case _:
            print("Opción no válida")
            menuPrincipal()
            
def main():
    connect()
    menuPrincipal()

if __name__ == '__main__':
    main()