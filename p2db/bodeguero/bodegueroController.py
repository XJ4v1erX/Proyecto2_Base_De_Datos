from bodeguero.bodegueroModel import actualizarCantida, consultaAlertas, consultaInventario, insertarSuministro


def menuBodeguero(idLugarMedico, idBodeguero):
    
    idBodeguero = idBodeguero
    idLugarMedico = idLugarMedico
    
    print(idLugarMedico)
    
    print('''
            \n
            ===============================
            |         Menú Bodeguero      |
            |-----------------------------|
            |   1. Ver inventario         |
            |   2. Ver alertas            |
            |   3. agregar suministro     |
            |   4. actualizar suministro  |
            |   5. Salir                  |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
    
    match opcion:
        case "1":
            verInventario(idLugarMedico, idBodeguero)
        case "2":
            verAlertas(idLugarMedico, idBodeguero)
        case "3":
            insertarInventario(idLugarMedico, idBodeguero)
        case "4":
            actualizarInventario(idLugarMedico, idBodeguero)
        case "5":
            print("Hasta luego")
        case _:
            print("Opción no válida")
            menuBodeguero(idLugarMedico, idBodeguero)
        
        
def verInventario(idLugarMedico, idBodeguero):
    inventario = consultaInventario(idLugarMedico, idBodeguero)
    if inventario:
        # Si la lista no está vacía, la imprimimos
        print("Cantidad de elementos en inventario: ", len(inventario))
        for item in inventario:
            print(item)
        input("Presione enter para continuar")
        menuBodeguero(idLugarMedico, idBodeguero)
    else:
        # Si la lista está vacía, mostramos el mensaje correspondiente
        print("No hay productos en el inventario")
        input("Presione enter para continuar")
        menuBodeguero(idLugarMedico, idBodeguero)



def verAlertas(idLugarMedico, idBodeguero):
    alertas = consultaAlertas(idLugarMedico, idBodeguero)
    if alertas:
        # Mostramos la cantidad de resultados obtenidos
        print("!ALERTA¡Cantidad de elementos en inventario con cantidad menor o igual a 15 y cerca de su fecha de caducidad: ", len(alertas))

        # Imprimimos los resultados
        for alerta in alertas:
            print(alerta)

        input("Presione enter para continuar")
        menuBodeguero(idLugarMedico, idBodeguero)
    else:
        print("No hay alertas ")
        input("Presione enter para continuar")
        menuBodeguero(idLugarMedico, idBodeguero)


def insertarInventario(idLugarMedico, idBodeguero):
    
    idSuministro= input("Ingrese el id del suministro: ")
    idLugarMedico= idLugarMedico
    cantidad= input("Ingrese la cantidad: ")
    expiracion= input("Ingrese la fecha de expiración: ")
    
    try:
        insertarSuministro(idSuministro, idLugarMedico, cantidad, expiracion)
        print("Suministro agregado exitosamente")
        input("Presione enter para continuar")
        menuBodeguero(idLugarMedico, idBodeguero)
    except:
        print("Error al agregar el suministro")
        input("Presione enter para continuar")
        menuBodeguero(idLugarMedico, idBodeguero)
        

def actualizarInventario(idLugarMedico, idBodeguero):
        
    idSuministro= input("Ingrese el id del suministro: ")
    idLugarMedico= idLugarMedico
    cantidad= input("Ingrese la cantidad: ")
        
    if actualizarCantida(idSuministro, idLugarMedico, cantidad):
        print("Suministro actualizado exitosamente")
        input("Presione enter para continuar")
        menuBodeguero( idLugarMedico, idBodeguero)
    else:
        print("Error al actualizar el suministro")
        input("Presione enter para continuar")
        menuBodeguero( idLugarMedico, idBodeguero)