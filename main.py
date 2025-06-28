from modelos.asignatura import Asignatura
from modelos.tipos_alumno import EstudianteDoctorado
from repositorios.repo_alumnos import RepositorioAlumnos
from repositorios.repo_asignaturas import RepositorioAsignaturas

if __name__ == "__main__":
    repo_alumnos = RepositorioAlumnos()
    repo_asig = RepositorioAsignaturas()

    # Crear asignaturas
    asig1 = Asignatura("Matemáticas", "MAT101", 5, "pregrado")
    asig2 = Asignatura("Investigación Avanzada", "INV501", 4, "doctorado")
    repo_asig.crear(asig1)
    repo_asig.crear(asig2)

    # Crear alumno
    alumno1 = EstudianteDoctorado("Juan Pérez", 30, "12345678-9", "1995-01-01")
    repo_alumnos.crear(alumno1)

    # Asignar asignaturas
    alumno1.agregar_asignatura(asig1)
    alumno1.agregar_asignatura(asig2)

    # Descargar notas
    alumno1.descargar_notas()

    # Mostrar rol
    recuperado = repo_alumnos.recuperar("12345678-9")
    if recuperado:
        print(f"Rol de {recuperado.nombre}: {recuperado.roles()}")

    # MODIFICAR alumno
    alumno_modificado = EstudianteDoctorado("Juan P. Modificado", 31, "12345678-9", "1994-12-31")
    repo_alumnos.modificar("12345678-9", alumno_modificado)

    # MODIFICAR asignatura
    asig_modificada = Asignatura("Matemáticas Avanzadas", "MAT101", 6, "pregrado")
    repo_asig.modificar("MAT101", asig_modificada)

    # ELIMINAR asignatura
    repo_asig.eliminar("INV501")

    # ELIMINAR alumno
    repo_alumnos.eliminar("12345678-9")
