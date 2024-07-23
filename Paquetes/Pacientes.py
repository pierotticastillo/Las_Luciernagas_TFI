import datetime
import json
import time
archivo_pacientes = "datos_pacientes.json"


def leer_archivo(nombre_arc):
    with open(nombre_arc, "rt", encoding="utf-8") as archivo_listo:
        archivo = archivo_listo.read()
        listado = json.loads(archivo)
        return listado


def cargar_archivo(nombre_arc, paciente):
    with open(nombre_arc, "wt", encoding="utf-8") as archivo_listo:
        listado = json.dumps(paciente)
        archivo_listo.write(listado)


def ver_paciente():
    pacientes = leer_archivo(archivo_pacientes)
    print(len(pacientes))
    print_paciente(pacientes)


def print_paciente(pacientes):
    anio = time.localtime().tm_year
    for paciente in pacientes:
        nacimiento = time.strptime(paciente["Nacimiento"], "%d/%m/%Y").tm_year
        edad = anio - nacimiento - 1
        edad = edad if edad >= 0 else 0
        ID = paciente["ID"]
        documento = paciente["Documento"]
        nombre = paciente["Apellido"] + " " + paciente["Nombre"]
        nacionalidad = paciente["Nacionalidad"]
        print(f"({ID}) {nombre} - {edad} años - {documento} - {nacionalidad}")


def cargar_paciente():
    opcion = input(
        "Presione enter para ingresar paciente, sino escriba'Fin': ")
    pacientes = leer_archivo(archivo_pacientes)
    while opcion.lower() != "fin":
        paciente = {
            "ID": max(pacientes, key=lambda a: a["ID"])["ID"] + 1,
            "Documento": input("Ingrese documento del paciente: "),
            "Apellido": input("Ingrese apellidos del paciente: ").upper(),
            "Nombre": input("Ingrese nombre del paciente: ").title(),
            "Nacimiento": input("Ingrese nacimiento del paciente en formato dd/mm/aaaa: "),
            "Nacionalidad": input("Ingrese nacionalidad del paciente: ").lower(),
            "Historia_clinica": []
        }
        pacientes.append(paciente)
        opcion = input(
            "Presione enter para ingresar paciente, sino escriba'Fin': ")

    cargar_archivo(archivo_pacientes, pacientes)


def modificar_paciente():
    pacientes = leer_archivo(archivo_pacientes)
    print_paciente(pacientes)
    consulta = input("Ingrese el numero del paciente: ")
    for paciente in pacientes:
        if int(paciente["ID"]) == int(consulta):
            modificar = int(input(
                "¿Qué desea modificar?\n1.-Documento\n2.-Apellidos\n3.-Nombres\n4.-Nacimiento\n5.-Nacionalidad\n0.-Para finalizar\n"))
            while (modificar != 0):
                match modificar:
                    case 1: paciente["Documento"] = input("Ingrese nuevo documento: ")
                    case 2: paciente["Apellido"] = input("Ingrese nuevo apellido: ").upper()
                    case 3: paciente["Nombre"] = input("Ingrese nuevo nombre: ").title()
                    case 4: paciente["Nacimiento"] = input("Ingrese nuevo nacimiento dd/mm/aaaa: ")
                    case 5: paciente["Nacionalidad"] = input("Ingrese nueva nacionalidad: ")
                modificar = int(input(
                    "¿Qué desea modificar?\n1.-Documento\n2.-Apellidos\n3.-Nombres\n4.-Nacimiento\n5.-Nacionalidad\n0.-Para finalizar\n"))
            cargar_archivo(archivo_pacientes, pacientes)
            return True
    print("La opcion no existe")


def eliminar_paciente():
    pacientes = leer_archivo(archivo_pacientes)
    print("Lista de pacientes")
    print_paciente(pacientes)
    eliminar = int(
        input("Ingrese el numero del paciente que desea eliminar: "))
    for paciente in pacientes:
        if int(paciente["ID"]) == int(eliminar):
            pacientes.remove(paciente)
            cargar_archivo(archivo_pacientes, pacientes)
    print("Paciente eliminado con éxito")


def ver_historiaclinica():
    pacientes = leer_archivo(archivo_pacientes)
    print_paciente(pacientes)
    indice = int(input("Ingrese ID del paciente: "))-1
    historia_clinica = pacientes[indice]["Historia_clinica"]
    print("Historia clinica")
    for i in historia_clinica:
        print("ID:", i["Id"], "\nFecha:", i["Fecha"], "\nEnfermedad:", i["Enfermedad"],
                "\nProfesional:", i["Profesional"], "\nObservaciones:", i["Observaciones"])


def agregar_historiaclinica():
    pacientes = leer_archivo(archivo_pacientes)
    print("¿A qué paciente desea agregarle historia clinica?")
    print_paciente(pacientes)
    consulta = int(input("Ingrese el ID del paciente: "))-1
    for paciente in pacientes:
        if int(paciente["ID"] == int(consulta)):
            historia = pacientes[consulta]["Historia_clinica"]
            longitud_lista_historia_clinica = len(historia)+1
            fecha_actual = datetime.datetime.now()
            fecha = datetime.datetime.strftime(fecha_actual, "%d/%m/%Y")
            enfermedad = input("Ingrese enfermedad o afección: ")
            profesional = input(
                "Ingrese apellido del profesional que lo atendió: ")
            observaciones = input("Ingrese Observaciones: ")
            historia.append({"Id": longitud_lista_historia_clinica,
                                "Fecha": fecha,
                                "Enfermedad": enfermedad.lower(),
                                "Profesional": profesional.upper(),
                                "Observaciones": observaciones})
    cargar_archivo(archivo_pacientes, pacientes)


def menu_historiaclinica():
    print("Bienvenido al Menú de Historias Clinicas\n Seleccione una opción:")
    opcion = int(
        input("1. Ver historia clinica\n2. Agregar historia clinica\n3. Salir"))
    match opcion:
        case 1:
            ver_historiaclinica()
        case 2:
            agregar_historiaclinica()
        case 3:
            exit


def buscar_apellido():
    pacientes = leer_archivo(archivo_pacientes)
    apellido = input("Ingrese Apellido del paciente: ")
    for paciente in pacientes:
        if (paciente["Apellido"] == (apellido.upper())):
            print("ID:", paciente["ID"], "\nApellido:", paciente["Apellido"], "\nNombre:", paciente["Nombre"], "\nNacimiento:", paciente["Nacimiento"], "\nDNI:", paciente["Documento"],
                    "\nNacionalidad:", paciente["Nacionalidad"], "\nHistoria Clinica:", paciente["Historia_clinica"])


def buscar_fechas():
    pacientes = leer_archivo(archivo_pacientes)
    fecha_inicial = input(
        "Ingrese fecha inicial del rango de busqueda en formato dd/mm/aaaa: ")
    fecha_final = input(
        "Ingrese fecha final del rango de busqueda en formato dd/mm/aaaa: ")

    formato_fecha_inicial = time.strptime(fecha_inicial, "%d/%m/%Y")
    formato_fecha_final = time.strptime(fecha_final, "%d/%m/%Y")

    for paciente in pacientes:
        for i in paciente["Historia_clinica"]:
            formato_fecha_paciente = time.strptime(i["Fecha"], "%d/%m/%Y")
            if (formato_fecha_inicial <= formato_fecha_paciente and formato_fecha_paciente <= formato_fecha_final):
                print(paciente)
    print("No hay pacientes atendidos en este rango de fechas")


def buscar_enfermedad():
    pacientes = leer_archivo(archivo_pacientes)
    enfermedad = input("Ingrese Enfermedad del paciente: ")
    for paciente in pacientes:
        for i in paciente["Historia_clinica"]:
            if (i["Enfermedad"] == enfermedad.lower()):
                print(paciente)


def buscar_profesional():
    pacientes = leer_archivo(archivo_pacientes)
    profesional = input(
        "Ingrese el apellido del profesional que atendio al paciente: ")
    for paciente in pacientes:
        for i in paciente["Historia_clinica"]:
            if (i["Profesional"] == profesional.upper()):
                print(paciente)


def buscar_nacionalidad():
    pacientes = leer_archivo(archivo_pacientes)
    nacionalidad = input("Ingrese Nacionalidad del paciente: ")
    for paciente in pacientes:
        if (paciente["Nacionalidad"] == (nacionalidad.lower())):
            print("ID:", paciente["ID"], "\nApellido:", paciente["Apellido"], "\nNombre:", paciente["Nombre"], "\nNacimiento:", paciente["Nacimiento"], "\nDNI:", paciente["Documento"],
                    "\nNacionalidad:", paciente["Nacionalidad"], "\nHistoria Clinica:", paciente["Historia_clinica"])


def menu_busqueda_paciente():
    print("Bienvenido al Menú de Búsqueda de un Paciente\n Seleccione una opción:")
    opcion = int(
        input("1. Buscar por Apellido\n2. Buscar por rango de fechas\n3. Buscar por Enfermedad\n4. Buscar por Profesional\n5. Buscar por Nacionalidad\n6. Salir\n"))
    match opcion:
        case 1:
            buscar_apellido()
        case 2:
            buscar_fechas()
        case 3:
            buscar_enfermedad()
        case 4:
            buscar_profesional()
        case 5:
            buscar_nacionalidad()
        case 6:
            exit


def menu_pacientes():
    print("""¿Qué acción desea realizar?
            1. Ver paciente en la base de datos.
            2. Registrar paciente en la base de datos.
            3. Modificar paciente en la base de datos.
            4. Eliminar paciente en la base de datos
            5. Historia Clínica
            6. Busqueda pacientes""")
    opcion = int(input("Ingrese opción, por favor: "))
    match opcion:
        case 1:
            ver_paciente()
        case 2:
            cargar_paciente()
        case 3:
            modificar_paciente()
        case 4:
            eliminar_paciente()
        case 5:
            menu_historiaclinica()
        case 6:
            menu_busqueda_paciente()
