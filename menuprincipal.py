from Paquetes import Profesionales as Profesion
from Paquetes import Pacientes as Paciente

print("""
      ***************************************
      *          Bienvenido al              *
      * Instituto Médico de las Luciernagas *
      ***************************************""")

print("")


def menu_principal():
    print("""
            Menu principal \n """)
    opcion = input(
        """Elija una opcion: \n 1-Pacientes \n 2-Profesionales \n 3-Cerrar \n \n Ingrese opción: """)
    if opcion == '1':
        Paciente.menu_pacientes()

    elif opcion == '2':
        Profesion.menu_profesionales()

    elif opcion == '3':
        print('Programa Cerrado')
        quit()
        return # Salir del bucle del menú

    else:
        print("Opción no válida. Por favor, elija 1, 2 o 3.")
    
    input("\nPresione Enter para continuar...") # Pausa para que el usuario vea el mensaje

while True:
    menu_principal()
