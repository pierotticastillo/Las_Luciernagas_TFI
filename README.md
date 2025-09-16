# Las_Luciernagas_TPI

- 📚 **Asignatura:** Programación I
- 📝 **Cáracter:** Trabajo Práctico Integrador
- 🎓 **Carrera:** Tecnicatura Universitaria en Desarrollo Web
- 🏛️ **Facultad de Ciencias de la Administración - UNER**

# Integrantes:
- 👩‍💻 KLOSTER, Micaela
- 👨‍💻 PIEROTTI CASTILLO, Enrique Alejandro

# Descripción del Proyecto:
Este proyecto es una solución de software tipo historia clínica para el "Instituto Médico Las Luciérnagas".

## Datos a Registrar:

### Pacientes:
- Documento de Identidad
- Apellido
- Nombre
- Fecha de Nacimiento
- Nacionalidad

### Historia Clínica (asociada a cada paciente):
- Fecha
- Enfermedad/afección que padece
- Médico del instituto que lo trató
- Observaciones

### Profesionales (en archivo diferente):
- Apellido
- Nombre
- Especialidad

## Requerimientos:

### Almacenamiento de Datos:
- La información de Pacientes e Historias Clínicas debe ser registrada en archivos en formato JSON.

### Interfaces de Usuario Interactivas:
- **Pacientes:**
    - Registrar uno nuevo.
    - Editar los datos de uno existente.
    - Eliminar un paciente.
- **Historias Clínicas:**
    - Agregar una historia clínica a un paciente.

### Funciones de Búsqueda de Pacientes:
- Apellido y/o Nombre
- Rango de fechas en la que fueron atendidos (Fecha de Historia clínica)
- Enfermedad/afección
- Por Médico que lo/la trató
- Nacionalidad

### Cálculos y Asignaciones Automáticas:
- En cada oportunidad que se muestren los datos de un paciente, se deberá calcular su edad a partir de su fecha de nacimiento y la fecha actual del sistema.
- Cada nuevo paciente tendrá asignado un número de Historia Clínica incremental que inicia en 1.

### Médicos:
- Permitir listar los existentes y registrar nuevos.

## Licencia:
Este proyecto está bajo la Licencia [MIT](./LICENSE).
