
from medico.medicoModel import actualizarHistorial, actualizarMedicina, actualizarPaciente, consultaHistorial, consultaPaciente, insertarHistorial, insertarPaciente


def menuMedico(idMedico):

    idMedico = idMedico
    
    print('''
            \n
            ===============================
            |         Menú Medico         |
            |-----------------------------|
            |   1. Pacientes              |
            |   2. Historial              |  
            |   3. Salir                  |
            ===============================
            ''')  
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            menuPacientes(idMedico)
        case "2":
            menuHistorial(idMedico)
        case "3":
            print("Hasta luego")
        case _:
            print("Opción no válida")
            menuMedico(idMedico)
            
            

def menuPacientes(idMedico):
    print('''
            \n
            ===============================
            |    Menú Medico Pacientes    |
            |-----------------------------|
            |   1. ver paciente           |
            |   2. ingresar paciente      | 
            |   3. editar paciente        | 
            |   4. regresar               |
            ===============================
            ''')  
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            verPaciente(idMedico)
        case "2":
            ingresarPaciente(idMedico)
        case "3":
            editarPaciente(idMedico)
        case "4":
            menuMedico(idMedico)
        case _:
            print("Opción no válida")
            menuMedico(idMedico)
            
def verPaciente(idMedico):
    idPaciente = input("Ingrese el id del paciente: ")
    
    if consultaPaciente(idPaciente) != None:
        print(consultaPaciente(idPaciente))
        input("Presione enter para continuar")
        menuPacientes(idMedico)
    else:
        print("No se pudo encontrar el paciente")
        input("Presione enter para continuar")
        menuPacientes(idMedico)
        
def ingresarPaciente(idMedico):
    
    nombre = input("Ingrese el nombre del paciente: ")
    direccion = input("Ingrese la dirección del paciente: ")
    telefono = input("Ingrese el teléfono del paciente: ")
    masaCorporal = input("Ingrese la masa corporal del paciente: ")
    altura = input("Ingrese la altura del paciente: ")
    adicciones = input("Ingrese las adicciones del paciente: ")
    
    if insertarPaciente(nombre, direccion, telefono, masaCorporal, altura, adicciones) != None:
        print("Paciente ingresado")
        input("Presione enter para continuar")
        menuPacientes(idMedico)
    else:
        print("No se pudo ingresar el paciente")
        input("Presione enter para continuar")
        menuPacientes(idMedico)
    
def editarPaciente(idMedico):
    
    idPaciente = input("Ingrese el id del paciente: ")
    
    if consultaPaciente(idPaciente) != None:
        print(consultaPaciente(idPaciente))
        nombre = input("Ingrese el nombre del paciente: ")
        direccion = input("Ingrese la dirección del paciente: ")
        telefono = input("Ingrese el teléfono del paciente: ")
        masaCorporal = input("Ingrese la masa corporal del paciente: ")
        altura = input("Ingrese la altura del paciente: ")
        adicciones = input("Ingrese las adicciones del paciente: ")
        
        if actualizarPaciente(idPaciente, nombre, direccion, telefono, masaCorporal, altura, adicciones) == True:
            print("Paciente editado")
            input("Presione enter para continuar")
            menuPacientes(idMedico)
        else:
            print("No se pudo editar el paciente")
            input("Presione enter para continuar")
            menuPacientes(idMedico)
    else:
        print("No se pudo encontrar el paciente")
        input("Presione enter para continuar")
        menuPacientes(idMedico)


def menuHistorial(idMedico):
    print('''
            \n
            ===============================
            |    Menú Medico Historial    |
            |-----------------------------|
            |   1. ver hisrorial          |
            |   2. ingresar historial     | 
            |   3. editar historial       | 
            |   4. regresar               |
            ===============================
            ''')  
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            verHistorial(idMedico)
        case "2":
            ingresarHistorial(idMedico)
        case "3":
            editarHistorial(idMedico)
        case "4":
            menuMedico(idMedico)
        case _:
            print("Opción no válida")
            menuMedico(idMedico)

def verHistorial(idMedico):
    idHistorial = input("Ingrese el id del paciente: ")
    
    if consultaHistorial(idHistorial) != None:
        print(consultaHistorial(idHistorial))
        input("Presione enter para continuar")
        menuHistorial(idMedico)
    else:
        print("No se pudo encontrar el historial")
        input("Presione enter para continuar")
        menuHistorial(idMedico)
    
def ingresarHistorial(idMedico):
    
    fecha = input("Ingrese la fecha del historial: ")
    herencias = input("Ingrese la herencias: ")
    tratamiento = input("Ingrese el id del suministro medico: ")
    cantidadMedicamento = input("Ingrese la cantidad del suministro medico: ")
    estado = input("Ingrese el estado del historial: ")
    comentario = input("Ingrese los comentarios del historial: ")
    idLugarMedico = input("Ingrese el id del lugar medico: ")
    idPaciente = input("Ingrese el id del paciente: ")
    idEnfermedad = input("Ingrese el id de la enfermedad: ")
    idMedico = idMedico
    
    if  insertarHistorial(fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico) and actualizarMedicina(cantidadMedicamento,tratamiento, idLugarMedico)== True:
        print("Historial ingresado")
        input("Presione enter para continuar")
        menuHistorial(idMedico)
    else:
        print("No se pudo ingresar el historial")
        input("Presione enter para continuar")
        menuHistorial(idMedico)
        
def editarHistorial(idMedico):
    
    idHistorial = input("Ingrese el id del historial: ")
    
    if consultaHistorial(idHistorial) != None:
        
        if consultaHistorial(idHistorial) != None:
            print(consultaHistorial(idHistorial))
            fecha = input("Ingrese la fecha del historial: ")
            herencias = input("Ingrese la herencias: ")
            tratamiento = input("Ingrese el tratamiento del historial: ")
            cantidadMedicamento = input("Ingrese la evolucion del historial: ")
            estado = input("Ingrese el estado del historial: ")
            comentario = input("Ingrese los comentarios del historial: ")
            idLugarMedico = input("Ingrese el id del lugar medico: ")
            idPaciente = input("Ingrese el id del paciente: ")
            idEnfermedad = input("Ingrese el id de la enfermedad: ")
            idMedico = idMedico
            
            if actualizarHistorial(idHistorial, fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico) and actualizarMedicina(cantidadMedicamento,tratamiento, idLugarMedico)  == True:
                print("Historial editado")
                input("Presione enter para continuar")
                menuHistorial(idMedico)
            else:
                print("No se pudo editar el historial")
                input("Presione enter para continuar")
                menuHistorial(idMedico)
        else:
            print("No se pudo encontrar el historial")
            input("Presione enter para continuar")
            menuHistorial(idMedico)