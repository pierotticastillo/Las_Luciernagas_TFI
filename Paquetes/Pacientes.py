import datetime
import json
import time
from datetime import date

archivo_pacientes = "datos_pacientes.json"


def leer_archivo(nombre_arc):
    try:
        with open(nombre_arc, "rt", encoding="utf-8") as archivo_listo:
            listado = json.load(archivo_listo)
            return listado
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{nombre_arc}' no se encontró. Se creará uno nuevo si se añaden datos.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_arc}' no tiene un formato JSON válido. Se inicializará con una lista vacía.")
        return []


def cargar_archivo(nombre_arc, paciente):
    with open(nombre_arc, "wt", encoding="utf-8") as archivo_listo:
        json.dump(paciente, archivo_listo, indent=4)


def calcular_edad(fecha_nacimiento_str):
    try:
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()
        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad
    except ValueError:
        return -1 # Indicar error en el formato de fecha


def ver_paciente():
    pacientes = leer_archivo(archivo_pacientes)
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    print(f"Total de pacientes: {len(pacientes)}")
    print_paciente(pacientes)


def print_paciente(pacientes):
    for paciente in pacientes:
        edad = calcular_edad(paciente["Nacimiento"])
        edad_str = f"{edad} años" if edad != -1 else "Fecha de nacimiento inválida"
        ID = paciente["ID"]
        documento = paciente["Documento"]
        nombre_completo = paciente["Apellido"] + " " + paciente["Nombre"]
        nacionalidad = paciente["Nacionalidad"]
        print(f"({ID}) {nombre_completo} - {edad_str} - DNI: {documento} - Nacionalidad: {nacionalidad}")


def cargar_paciente():
    pacientes = leer_archivo(archivo_pacientes)
    while True:
        opcion = input("\nPresione Enter para ingresar un nuevo paciente, o escriba 'fin' para salir: ").lower()
        if opcion == "fin":
            break

        documento = input("Ingrese documento del paciente: ")
        apellido = input("Ingrese apellidos del paciente: ").upper()
        nombre = input("Ingrese nombre del paciente: ").title()
        nacimiento = input("Ingrese fecha de nacimiento del paciente en formato dd/mm/aaaa: ")
        nacionalidad = input("Ingrese nacionalidad del paciente: ").lower()

        if not pacientes:
            paciente_id = 1
        else:
            paciente_id = max(p["ID"] for p in pacientes) + 1

        paciente = {
            "ID": paciente_id,
            "Documento": documento,
            "Apellido": apellido,
            "Nombre": nombre,
            "Nacimiento": nacimiento,
            "Nacionalidad": nacionalidad,
            "Historia_clinica": []
        }
        pacientes.append(paciente)
        print(f"Paciente {nombre} {apellido} registrado con ID: {paciente_id}")

    cargar_archivo(archivo_pacientes, pacientes)
    print("Pacientes guardados exitosamente.")


def modificar_paciente():
    pacientes = leer_archivo(archivo_pacientes)
    if not pacientes:
        print("No hay pacientes para modificar.")
        return

    print_paciente(pacientes)
    try:
        consulta_id = int(input("Ingrese el ID del paciente a modificar: "))
    except ValueError:
        print("ID inválido. Por favor, ingrese un número.")
        return

    paciente_encontrado = None
    for paciente in pacientes:
        if paciente["ID"] == consulta_id:
            paciente_encontrado = paciente
            break

    if paciente_encontrado:
        while True:
            try:
                modificar = int(input(
                    "\n¿Qué desea modificar?\n1.-Documento\n2.-Apellidos\n3.-Nombres\n4.-Nacimiento\n5.-Nacionalidad\n0.-Para finalizar\nIngrese opción: "))
                if modificar == 0:
                    break
                match modificar:
                    case 1: paciente_encontrado["Documento"] = input("Ingrese nuevo documento: ")
                    case 2: paciente_encontrado["Apellido"] = input("Ingrese nuevo apellido: ").upper()
                    case 3: paciente_encontrado["Nombre"] = input("Ingrese nuevo nombre: ").title()
                    case 4: paciente_encontrado["Nacimiento"] = input("Ingrese nuevo nacimiento dd/mm/aaaa: ")
                    case 5: paciente_encontrado["Nacionalidad"] = input("Ingrese nueva nacionalidad: ")
                    case _: print("Opción no válida.")
            except ValueError:
                print("Opción inválida. Por favor, ingrese un número.")
        cargar_archivo(archivo_pacientes, pacientes)
        print(f"Paciente con ID {consulta_id} modificado con éxito.")
    else:
        print(f"No se encontró ningún paciente con el ID {consulta_id}.")


def eliminar_paciente():
    pacientes = leer_archivo(archivo_pacientes)
    if not pacientes:
        print("No hay pacientes para eliminar.")
        return

    print("Lista de pacientes:")
    print_paciente(pacientes)
    try:
        eliminar_id = int(input("Ingrese el ID del paciente que desea eliminar: "))
    except ValueError:
        print("ID inválido. Por favor, ingrese un número.")
        return

    pacientes_actualizados = [p for p in pacientes if p["ID"] != eliminar_id]

    if len(pacientes_actualizados) < len(pacientes):
        cargar_archivo(archivo_pacientes, pacientes_actualizados)
        print(f"Paciente con ID {eliminar_id} eliminado con éxito.")
    else:
        print(f"No se encontró ningún paciente con el ID {eliminar_id}.")


def ver_historiaclinica():
    pacientes = leer_archivo(archivo_pacientes)
    if not pacientes:
        print("No hay pacientes registrados para ver historias clínicas.")
        return

    print_paciente(pacientes)
    try:
        consulta_id = int(input("Ingrese ID del paciente para ver su historia clínica: "))
    except ValueError:
        print("ID inválido. Por favor, ingrese un número.")
        return

    paciente_encontrado = None
    for paciente in pacientes:
        if paciente["ID"] == consulta_id:
            paciente_encontrado = paciente
            break

    if paciente_encontrado:
        historia_clinica = paciente_encontrado["Historia_clinica"]
        if not historia_clinica:
            print(f"El paciente {paciente_encontrado['Nombre']} {paciente_encontrado['Apellido']} no tiene historias clínicas registradas.")
            return
        print(f"\nHistoria clínica de {paciente_encontrado['Nombre']} {paciente_encontrado['Apellido']}:")
        for h in historia_clinica:
            print(f"  ID Historia: {h['Id']}")
            print(f"  Fecha: {h['Fecha']}")
            print(f"  Enfermedad: {h['Enfermedad']}")
            print(f"  Profesional: {h['Profesional']}")
            print(f"  Observaciones: {h['Observaciones']}")
            print("-" * 30)
    else:
        print(f"No se encontró ningún paciente con el ID {consulta_id}.")


def agregar_historiaclinica():
    pacientes = leer_archivo(archivo_pacientes)
    if not pacientes:
        print("No hay pacientes registrados para agregar historias clínicas.")
        return

    print("¿A qué paciente desea agregarle historia clínica?")
    print_paciente(pacientes)
    try:
        consulta_id = int(input("Ingrese el ID del paciente: "))
    except ValueError:
        print("ID inválido. Por favor, ingrese un número.")
        return

    paciente_encontrado = None
    for paciente in pacientes:
        if paciente["ID"] == consulta_id:
            paciente_encontrado = paciente
            break

    if paciente_encontrado:
        historia = paciente_encontrado["Historia_clinica"]
        
        if not historia:
            historia_id = 1
        else:
            historia_id = max(h["Id"] for h in historia) + 1

        fecha_actual = datetime.datetime.now()
        fecha = datetime.datetime.strftime(fecha_actual, "%d/%m/%Y")
        enfermedad = input("Ingrese enfermedad o afección: ")
        profesional = input("Ingrese apellido del profesional que lo atendió: ")
        observaciones = input("Ingrese Observaciones: ")
        
        historia.append({
            "Id": historia_id,
            "Fecha": fecha,
            "Enfermedad": enfermedad.lower(),
            "Profesional": profesional.upper(),
            "Observaciones": observaciones
        })
        cargar_archivo(archivo_pacientes, pacientes)
        print(f"Historia clínica agregada al paciente {paciente_encontrado['Nombre']} {paciente_encontrado['Apellido']}.")
    else:
        print(f"No se encontró ningún paciente con el ID {consulta_id}.")


def menu_historiaclinica():
    while True:
        print("\nBienvenido al Menú de Historias Clínicas\n Seleccione una opción:")
        try:
            opcion = int(input("1. Ver historia clínica\n2. Agregar historia clínica\n3. Salir\nIngrese opción: "))
            match opcion:
                case 1:
                    ver_historiaclinica()
                case 2:
                    agregar_historiaclinica()
                case 3:
                    return # Volver al menú anterior
                case _:
                    print("Opción no válida. Por favor, elija 1, 2 o 3.")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número.")
        input("\nPresione Enter para continuar...")


def buscar_pacientes_generico(criterio, valor):
    pacientes = leer_archivo(archivo_pacientes)
    resultados = []
    for paciente in pacientes:
        if criterio == "apellido_nombre":
            nombre_completo = (paciente["Apellido"] + " " + paciente["Nombre"]).lower()
            if valor.lower() in nombre_completo:
                resultados.append(paciente)
        elif criterio == "nacionalidad":
            if paciente["Nacionalidad"].lower() == valor.lower():
                resultados.append(paciente)
        elif criterio == "enfermedad":
            for h in paciente["Historia_clinica"]:
                if h["Enfermedad"].lower() == valor.lower():
                    resultados.append(paciente)
                    break # Para no añadir el mismo paciente varias veces
        elif criterio == "profesional":
            for h in paciente["Historia_clinica"]:
                if h["Profesional"].upper() == valor.upper():
                    resultados.append(paciente)
                    break
    return resultados


def buscar_apellido_nombre():
    valor_busqueda = input("Ingrese Apellido y/o Nombre del paciente a buscar: ")
    resultados = buscar_pacientes_generico("apellido_nombre", valor_busqueda)
    if resultados:
        print("\nPacientes encontrados:")
        print_paciente(resultados)
    else:
        print("No se encontraron pacientes con ese apellido y/o nombre.")


def buscar_fechas():
    pacientes = leer_archivo(archivo_pacientes)
    try:
        fecha_inicial_str = input("Ingrese fecha inicial del rango de búsqueda (dd/mm/aaaa): ")
        fecha_final_str = input("Ingrese fecha final del rango de búsqueda (dd/mm/aaaa): ")

        formato_fecha_inicial = datetime.datetime.strptime(fecha_inicial_str, "%d/%m/%Y").date()
        formato_fecha_final = datetime.datetime.strptime(fecha_final_str, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de fecha inválido. Use dd/mm/aaaa.")
        return

    resultados = []
    for paciente in pacientes:
        for h in paciente["Historia_clinica"]:
            try:
                fecha_historia = datetime.datetime.strptime(h["Fecha"], "%d/%m/%Y").date()
                if formato_fecha_inicial <= fecha_historia <= formato_fecha_final:
                    resultados.append(paciente)
                    break # Para no añadir el mismo paciente varias veces
            except ValueError:
                print(f"Advertencia: Fecha de historia clínica inválida para el paciente ID {paciente['ID']}.")
                continue
    
    if resultados:
        print("\nPacientes atendidos en este rango de fechas:")
        print_paciente(resultados)
    else:
        print("No hay pacientes atendidos en este rango de fechas.")


def buscar_enfermedad():
    enfermedad = input("Ingrese la enfermedad o afección a buscar: ")
    resultados = buscar_pacientes_generico("enfermedad", enfermedad)
    if resultados:
        print("\nPacientes encontrados con esa enfermedad:")
        print_paciente(resultados)
    else:
        print("No se encontraron pacientes con esa enfermedad.")


def buscar_profesional():
    profesional = input("Ingrese el apellido del profesional que atendió al paciente: ")
    resultados = buscar_pacientes_generico("profesional", profesional)
    if resultados:
        print("\nPacientes encontrados atendidos por ese profesional:")
        print_paciente(resultados)
    else:
        print("No se encontraron pacientes atendidos por ese profesional.")


def buscar_nacionalidad():
    nacionalidad = input("Ingrese la nacionalidad a buscar: ")
    resultados = buscar_pacientes_generico("nacionalidad", nacionalidad)
    if resultados:
        print("\nPacientes encontrados con esa nacionalidad:")
        print_paciente(resultados)
    else:
        print("No se encontraron pacientes con esa nacionalidad.")


def menu_busqueda_paciente():
    while True:
        print("\nBienvenido al Menú de Búsqueda de un Paciente\n Seleccione una opción:")
        try:
            opcion = int(input("1. Buscar por Apellido y/o Nombre\n2. Buscar por rango de fechas de atención\n3. Buscar por Enfermedad\n4. Buscar por Profesional\n5. Buscar por Nacionalidad\n6. Salir\nIngrese opción: "))
            match opcion:
                case 1:
                    buscar_apellido_nombre()
                case 2:
                    buscar_fechas()
                case 3:
                    buscar_enfermedad()
                case 4:
                    buscar_profesional()
                case 5:
                    buscar_nacionalidad()
                case 6:
                    return # Volver al menú anterior
                case _:
                    print("Opción no válida. Por favor, elija una opción entre 1 y 6.")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número.")
        input("\nPresione Enter para continuar...")


def menu_pacientes():
    while True:
        print("\n--- Menú de Pacientes ---")
        print("""¿Qué acción desea realizar?
            1. Ver pacientes en la base de datos.
            2. Registrar nuevo paciente.
            3. Modificar paciente existente.
            4. Eliminar paciente.
            5. Gestionar Historias Clínicas.
            6. Buscar pacientes.
            7. Volver al Menú Principal.""")
        try:
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
                case 7:
                    return # Volver al menú principal
                case _:
                    print("Opción no válida. Por favor, elija una opción entre 1 y 7.")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número.")
        input("\nPresione Enter para continuar...")
