import json

archivo_profesionales = "Profesionales.json"

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

def cargar_archivo(nombre_arc, profesionales):
    with open(nombre_arc, "wt", encoding="utf-8") as archivo_listo:
        json.dump(profesionales, archivo_listo, indent=4)

def ver_profesional():
    profesionales = leer_archivo(archivo_profesionales)
    if not profesionales:
        print("No hay profesionales registrados.")
        return
    print('\nLista de profesionales:')
    for prof in profesionales:
        print(f"Nombre: {prof['Nombre']}, Apellido: {prof['Apellido']}, Especialidad: {prof['Especialidad']}")
    print("-" * 30)
    
def agregar_profesional():
    profesionales = leer_archivo(archivo_profesionales)
    nombre = input('Ingresar Nombre: ')
    apellido = input('Ingrese el Apellido: ')
    especialidad = input('Ingrese la Especialidad: ')
    
    profesionales.append({
        "Nombre": nombre.title(),
        "Apellido": apellido.upper(),
        "Especialidad": especialidad.title()
    })
    cargar_archivo(archivo_profesionales, profesionales)
    print(f"Profesional {nombre} {apellido} registrado con éxito.")

def menu_profesionales():
    while True:
        print("\n--- Menú de Profesionales ---")
        print("""¿Qué acción desea realizar?
            1. Ver profesionales en la base de datos.
            2. Registrar nuevo profesional.
            3. Volver al Menú Principal.""")
        try:
            opcion = int(input("Ingrese opción, por favor: "))
            match opcion:
                case 1:
                    ver_profesional()
                case 2:
                    agregar_profesional()
                case 3:
                    return # Volver al menú principal
                case _:
                    print("Opción no válida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número.")
        input("\nPresione Enter para continuar...")
