Portafolios MDAnálisis

Este repositorio contiene los talleres desarrollados para la asignatura Metodología de Diseño. Cada taller está organizado en su propia carpeta.

Taller 1: Principios SOLID

El Taller 1 implementa un sistema de gestión de alumnos y asignaturas aplicando los principios SOLID.

El sistema permite:
- Crear, recuperar (listar), modificar y eliminar alumnos por RUT.
- Crear, recuperar (listar), modificar y eliminar asignaturas por código.
- Asignar asignaturas a alumnos.
- Descargar notas simuladas de las asignaturas del alumno (por ejemplo, muestra 7.0 como nota fija).
- Simular almacenamiento en base de datos usando diccionarios y mensajes por consola (print).
- Usar distintos tipos de alumno:
  - Titulado
  - Estudiante no ayudante
  - Estudiante ayudante
  - Estudiante magíster
  - Estudiante doctorado

Supuestos:
- Las asignaturas pueden tener tipo pregrado, magister, doctorado o general.
- Cualquier tipo de alumno puede inscribir cualquier asignatura. No se validan requisitos de inscripción.
- Las notas se simulan con un valor fijo (7.0) y no se almacenan calificaciones reales.

Ejecución:
2. Navegar a la carpeta:
   cd Portafolios-MDAnalisis/Taller1_SOLID
3. Ejecutar:
   python main.py

Principios SOLID aplicados:
- Responsabilidad única: cada clase tiene una única función clara.
- Abierto/cerrado: se pueden agregar nuevos tipos de alumno sin modificar el código existente.
- Sustitución de Liskov: los tipos de alumno sustituyen correctamente a la clase base Alumno.
- Segregación de interfaces: las clases solo tienen los métodos que necesitan.
- Inversión de dependencias: los repositorios desacoplan la lógica de almacenamiento de los modelos.

Acceso:
El repositorio incluye acceso para el colaborador @MrNeo44.
