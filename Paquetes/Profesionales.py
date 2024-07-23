import json

def ver_profesional():
    with open ('Profesionales.json', 'rt', encoding="utf-8") as prof:
            Profesionales=json.load(prof)
            print('Lista de profesionales:')
            for i in Profesionales:
                print(i, '\n')
           
def agregar_profesional():
    nombre = input('Ingresar Nombre: ')
    apellido = input('Ingrese el Apellido: ')
    especialidad = input('Ingrese la Especialidad: ')
    with open ('Profesionales.json','rt',encoding='utf-8') as agreg:
        datos = agreg.read()
        carga=json.loads(datos)
        carga.append({
            "Nombre": nombre.title(),
            "Apellido": apellido.upper(),
            "Especialidad": especialidad.title()})
        with open(f'profesionales.json', 'wt',encoding='utf-8') as file:
            json.dump(carga, file, indent= 4)

def menu_profesionales():
    print("""¿Qué acción desea realizar?
            1. Ver profesionales en la base de datos.
            2. Registrar profesional en la base de datos.""")
    opcion = int(input("Ingrese opción, por favor: "))
    match opcion:
        case 1:
            ver_profesional()
        case 2:
            agregar_profesional()