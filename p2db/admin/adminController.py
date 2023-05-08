from admin.adminModel import actualizarBodeguero, actualizarHistorial, actualizarHospital, actualizarMedicina, actualizarMedico, actualizarPaciente, consultaBodeguero, consultaEnfermedadesMasFrecuentesMuerte, consultaHistorial, consultaHospital, consultaInventarioBajo, consultaMedico, consultaPaciente, consultaPacientesAtendidos, consultaTopPacientes, consultarPacientesPorMedico, ingresarHospital, insertarHistorial, insertarPaciente
from crearCuenta.crearCuentaController import crearBodeguero, crearMedico


def menuAdmin():
    
    print('''
            \n
            ===============================
            |         Menú admin          |
            |-----------------------------|
            |   1. Pacientes              |
            |   2. historiales            |
            |   3. Medicos                |
            |   4. Bodegueros             |
            |   5. Hospital               |
            |   6. Reportes               |
            |   7. Salir                  |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            pacientesMenu()
        case "2":
            historialMenu()
        case "3":
            medicoMenu()
        case "4":
            bodegueroMenu()
        case "5":
            hospitalMenu()  
        case "6":
            reportesMenu()
        case "7":
            print("Hasta luego")
        case _:
            print("Opción no válida")
            menuAdmin()

def pacientesMenu():
    print('''
            \n
            ===============================
            |       Menú  Pacientes       |
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
            verPaciente()
        case "2":
            ingresarPaciente()
        case "3":
            editarPaciente()
        case "4":
            menuAdmin()
        case _:
            print("Opción no válida")
            pacientesMenu()
            
def verPaciente():
    idPaciente = input("Ingrese el id del paciente: ")
    
    if consultaPaciente(idPaciente) != None:
        print(consultaPaciente(idPaciente))
        input("Presione enter para continuar")
        pacientesMenu()
    else:
        print("No se pudo encontrar el paciente")
        input("Presione enter para continuar")
        pacientesMenu()
        
def ingresarPaciente():
    
    nombre = input("Ingrese el nombre del paciente: ")
    direccion = input("Ingrese la dirección del paciente: ")
    telefono = input("Ingrese el teléfono del paciente: ")
    masaCorporal = input("Ingrese la masa corporal del paciente: ")
    altura = input("Ingrese la altura del paciente: ")
    adicciones = input("Ingrese las adicciones del paciente: ")
    
    if insertarPaciente(nombre, direccion, telefono, masaCorporal, altura, adicciones) != None:
        print("Paciente ingresado")
        input("Presione enter para continuar")
        pacientesMenu()
    else:
        print("No se pudo ingresar el paciente")
        input("Presione enter para continuar")
        pacientesMenu()
    
def editarPaciente():
    
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
            pacientesMenu()
        else:
            print("No se pudo editar el paciente")
            input("Presione enter para continuar")
            pacientesMenu()
    else:
        print("No se pudo encontrar el paciente")
        input("Presione enter para continuar")
        pacientesMenu()


def historialMenu():
    print('''
            \n
            ===============================
            |       Menú Historial        |
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
            verHistorial()
        case "2":
            ingresarHistorial()
        case "3":
            editarHistorial()
        case "4":
            menuAdmin()
        case _:
            print("Opción no válida")
            historialMenu()

def verHistorial():
    idHistorial = input("Ingrese el id del paciente: ")
    
    if consultaHistorial(idHistorial) != None:
        print(consultaHistorial(idHistorial))
        input("Presione enter para continuar")
        historialMenu()
    else:
        print("No se pudo encontrar el historial")
        input("Presione enter para continuar")
        historialMenu()
    
def ingresarHistorial():
    
    fecha = input("Ingrese la fecha del historial: ")
    herencias = input("Ingrese la herencias: ")
    tratamiento = input("Ingrese el id del suministro medico: ")
    cantidadMedicamento = input("Ingrese la cantidad del suministro medico: ")
    estado = input("Ingrese el estado del historial: ")
    comentario = input("Ingrese los comentarios del historial: ")
    idLugarMedico = input("Ingrese el id del lugar medico: ")
    idPaciente = input("Ingrese el id del paciente: ")
    idEnfermedad = input("Ingrese el id de la enfermedad: ")
    idMedico= input("Ingrese el id del medico: ") 
    
    if  insertarHistorial(fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad,idMedico ) and actualizarMedicina(cantidadMedicamento,tratamiento, idLugarMedico) == True:
        print("Historial ingresado")
        input("Presione enter para continuar")
        historialMenu()
    else:
        print("No se pudo ingresar el historial")
        input("Presione enter para continuar")
        historialMenu()
        
def editarHistorial():
    
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
            idMedico=  input("Ingrese el id del medico: ")
            
            if actualizarHistorial(idHistorial, fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico)and actualizarMedicina(cantidadMedicamento,tratamiento, idLugarMedico)  == True:
                print("Historial editado")
                input("Presione enter para continuar")
                historialMenu()
            else:
                print("No se pudo editar el historial")
                input("Presione enter para continuar")
                historialMenu()
        else:
            print("No se pudo encontrar el historial")
            input("Presione enter para continuar")
            historialMenu()

def medicoMenu():
    
    print('''
            \n
            ===============================
            |       Menú Medico           |
            |-----------------------------|
            |   1. ver medico             |
            |   2. ingresar medico        | 
            |   3. editar medico          | 
            |   4. regresar               |
            ===============================
            ''')  
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            verMedico()
        case "2":
            crearMedico()
        case "3":
            editarMedico()
        case "4":
            menuAdmin()
        case _:
            print("Opción no válida")
            medicoMenu()
    

def verMedico():
    idMedico = input("Ingrese el id del medico: ")
    
    if consultaMedico(idMedico) != None:
        print(consultaMedico(idMedico))
        input("Presione enter para continuar")
        medicoMenu()
    
    else:
        print("No se pudo encontrar el medico")
        input("Presione enter para continuar")
        medicoMenu()
        
def editarMedico():
    
    idMedico = input("Ingrese el id del medico: ")
    
    if consultaMedico(idMedico) != None:
        print(consultaMedico(idMedico))
        nombre = input("Ingrese el nombre del medico: ")
        direccion = input("Ingrese la dirección del medico: ")
        telefono = input("Ingrese el teléfono del medico: ")
        especialidad = input("Ingrese la especialidad del medico: ")
        idLugarMedico = input("Ingrese el id del lugar medico: ")
        
        if actualizarMedico(idMedico, nombre, direccion, telefono, especialidad, idLugarMedico) == True:
            print("Medico editado")
            input("Presione enter para continuar")
            medicoMenu()
        else:
            print("No se pudo editar el medico")
            input("Presione enter para continuar")
            medicoMenu()
    else:
        print("No se pudo encontrar el medico")
        input("Presione enter para continuar")
        medicoMenu()


def bodegueroMenu():
    
    print('''
            \n
            ===============================
            |       Menú Bodeguero        |
            |-----------------------------|
            |   1. ver Bodeguero          |
            |   2. ingresar Bodeguero     | 
            |   3. editar Bodeguero       | 
            |   4. regresar               |
            ===============================
            ''')  
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            verBodeguero()
        case "2":
            crearBodeguero()
        case "3":
            editarBodeguero()
        case "4":
            menuAdmin()
        case _:
            print("Opción no válida")
            bodegueroMenu()
    

def verBodeguero():
    idBodeguero = input("Ingrese el id del bodeguero: ")
    
    if consultaBodeguero(idBodeguero) != None:
        print(consultaBodeguero(idBodeguero))
        input("Presione enter para continuar")
        bodegueroMenu()
        
    else:
        print("No se pudo encontrar el bodeguero")
        input("Presione enter para continuar")
        bodegueroMenu()
    
def editarBodeguero():
    
    idBodeguero = input("Ingrese el id del bodeguero: ")
    
    if consultaMedico(idBodeguero) != None:
        print(consultaMedico(idBodeguero))
        nombre = input("Ingrese su nombre: ")
        idLugarMedico = input("Ingrese su LLugar Medico en el que trabaja: ")
        
        if actualizarBodeguero(idBodeguero, nombre, idLugarMedico) == True:
            print("Bodeguero editado")
            input("Presione enter para continuar")
            bodegueroMenu()
        
        else :
            print("No se pudo editar el bodeguero")
            input("Presione enter para continuar")
            bodegueroMenu()
    else:
        print("No se pudo encontrar el bodeguero")
        input("Presione enter para continuar")
        bodegueroMenu()
        

def hospitalMenu():

    
    print('''
            \n
            ===============================
            |       Menú Hospital         |
            |-----------------------------|
            |   1. ver Hospital           |
            |   2. ingresar Hospital      | 
            |   3. editar Hospital        | 
            |   4. regresar               |
            ===============================
            ''')  
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            verHospital()
        case "2":
            crearHospital()
        case "3":
            editarHospital()
        case "4":
            menuAdmin()
        case _:
            print("Opción no válida")
            hospitalMenu()

def verHospital():
    
    idLUgarMedico = input("Ingrese el id del lugar medico: ")
    
    if consultaHospital(idLUgarMedico) != None:
        print(consultaHospital(idLUgarMedico))
        input("Presione enter para continuar")
        hospitalMenu()
        
    else:
        print("No se pudo encontrar el hospital")
        input("Presione enter para continuar")
        hospitalMenu()

def crearHospital():

    nombre = input("Ingrese el nombre del hospital: ")
    localizacion = input("Ingrese la dirección del hospital: ")
    

    if ingresarHospital( nombre, localizacion) == True:
        print("Hospital ingresado")
        input("Presione enter para continuar")
        hospitalMenu()
    else:
        print("No se pudo ingresar el hospital")
        input("Presione enter para continuar")
        hospitalMenu()
        
def editarHospital():
    
    idLugarMedico = input("Ingrese el id del lugar medico: ")
    
    if consultaHospital(idLugarMedico) != None:
        print(consultaHospital(idLugarMedico))
        nombre = input("Ingrese el nombre del hospital: ")
        localizacion = input("Ingrese la dirección del hospital: ")
        
        if actualizarHospital(idLugarMedico, nombre, localizacion) != None:
            print("Hospital editado")
            input("Presione enter para continuar")
            hospitalMenu()
        else:
            print("No se pudo editar el hospital")
            input("Presione enter para continuar")
            hospitalMenu()
    else:
        print("No se pudo encontrar el hospital")
        input("Presione enter para continuar")
        hospitalMenu()
        
        

        
def reportesMenu():
    print('''
            \n
            ===============================
            |        Menú Reportes        |
            |-----------------------------|
            |   1. top 10 enfermedades    |
            |   2. to 10 medicos          | 
            |   3. top 5 pacientes        | 
            |   4. reporte medicina       |
            |   5. top 3 lugares medicos  |
            |   6. regresar               |
            ===============================
            ''')  
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            p1()
        case "2":
            p2()
        case "3":
            p3()
        case "4":
            p4()
        case "5":
            p5()
        case "6":
            menuAdmin()
        case _:
            print("Opción no válida")
            reportesMenu()


def p1():
    
    print("Top 10 enfermedades")
    print(consultaEnfermedadesMasFrecuentesMuerte())
    input("Presione enter para continuar")
    reportesMenu()
    
def p2():
    
    print("Top 10 medicos")
    print(consultarPacientesPorMedico())
    input("Presione enter para continuar")
    reportesMenu()
    
def p3():
    
    print("Top 5 pacientes")
    print(consultaTopPacientes())
    input("Presione enter para continuar")
    reportesMenu()

def p4():
    
    print("Reporte medicina")
    print(consultaInventarioBajo())
    input("Presione enter para continuar")
    reportesMenu()
    
def p5():
    
    print("Top 3 lugares medicos")
    print(consultaPacientesAtendidos())
    input("Presione enter para continuar")
    reportesMenu()
    