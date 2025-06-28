from modelos.asignatura import Asignatura
from modelos.tipos_alumno import (
    Titulado, EstudianteNoAyudante, EstudianteAyudante,
    EstudianteMagister, EstudianteDoctorado
)
from repositorios.repo_alumnos import RepositorioAlumnos
from repositorios.repo_asignaturas import RepositorioAsignaturas

def crear_alumno(repo):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    rut = input("RUT (formato xxxxxxxx-x): ")
    fecha = input("Fecha de nacimiento (DD/MM/AAAA): ")

    print("Tipo de alumno:")
    print("1. Titulado")
    print("2. Estudiante no ayudante")
    print("3. Estudiante ayudante")
    print("4. Estudiante magister")
    print("5. Estudiante doctorado")
    tipo = input("Selecciona el tipo (1-5): ")

    if tipo == "1":
        alumno = Titulado(nombre, edad, rut, fecha)
    elif tipo == "2":
        alumno = EstudianteNoAyudante(nombre, edad, rut, fecha)
    elif tipo == "3":
        alumno = EstudianteAyudante(nombre, edad, rut, fecha)
    elif tipo == "4":
        alumno = EstudianteMagister(nombre, edad, rut, fecha)
    elif tipo == "5":
        alumno = EstudianteDoctorado(nombre, edad, rut, fecha)
    else:
        print("Tipo inválido. No se creó el alumno.")
        return

    repo.crear(alumno)

def modificar_alumno(repo):
    rut = input("RUT del alumno a modificar: ")
    alumno_actual = repo.recuperar(rut)
    if not alumno_actual:
        print("Alumno no encontrado.")
        return

    print(f"Modificando alumno {alumno_actual.nombre}")
    nombre = input("Nuevo nombre: ")
    edad = int(input("Nueva edad: "))
    fecha = input("Nueva fecha de nacimiento (DD/MM/AAAA): ")

    print("Nuevo tipo de alumno:")
    print("1. Titulado")
    print("2. Estudiante no ayudante")
    print("3. Estudiante ayudante")
    print("4. Estudiante magister")
    print("5. Estudiante doctorado")
    tipo = input("Selecciona el tipo (1-5): ")

    if tipo == "1":
        alumno = Titulado(nombre, edad, rut, fecha)
    elif tipo == "2":
        alumno = EstudianteNoAyudante(nombre, edad, rut, fecha)
    elif tipo == "3":
        alumno = EstudianteAyudante(nombre, edad, rut, fecha)
    elif tipo == "4":
        alumno = EstudianteMagister(nombre, edad, rut, fecha)
    elif tipo == "5":
        alumno = EstudianteDoctorado(nombre, edad, rut, fecha)
    else:
        print("Tipo inválido. No se modificó el alumno.")
        return

    repo.modificar(rut, alumno)

def crear_asignatura(repo):
    nombre = input("Nombre de la asignatura: ")
    codigo = input("Código (por ejemplo ICI-101): ")
    creditos = int(input("Créditos: "))
    tipo = input("Tipo (pregrado, magister, doctorado, general): ").lower()
    asig = Asignatura(nombre, codigo, creditos, tipo)
    repo.crear(asig)

def modificar_asignatura(repo):
    codigo = input("Código de la asignatura a modificar: ")
    asig_actual = repo.recuperar(codigo)
    if not asig_actual:
        print("Asignatura no encontrada.")
        return

    print(f"Modificando asignatura {asig_actual.nombre}")
    nombre = input("Nuevo nombre: ")
    creditos = int(input("Nuevos créditos: "))
    tipo = input("Nuevo tipo (pregrado, magister, doctorado, general): ").lower()
    nueva = Asignatura(nombre, codigo, creditos, tipo)
    repo.modificar(codigo, nueva)

def asignar_asignatura_alumno(repo_alumnos, repo_asig):
    rut = input("RUT del alumno: ")
    alumno = repo_alumnos.recuperar(rut)
    if not alumno:
        print("Alumno no encontrado.")
        return

    codigo = input("Código de la asignatura: ")
    asig = repo_asig.recuperar(codigo)
    if not asig:
        print("Asignatura no encontrada.")
        return

    alumno.agregar_asignatura(asig)
    print(f"Asignatura {asig.nombre} asignada a {alumno.nombre}.")

def descargar_notas(repo_alumnos):
    rut = input("RUT del alumno: ")
    alumno = repo_alumnos.recuperar(rut)
    if not alumno:
        print("Alumno no encontrado.")
        return

    alumno.descargar_notas()

def menu():
    repo_alumnos = RepositorioAlumnos()
    repo_asig = RepositorioAsignaturas()

    while True:
        print("\nMenú")
        print("1. Crear alumno")
        print("2. Modificar alumno")
        print("3. Eliminar alumno")
        print("4. Crear asignatura")
        print("5. Modificar asignatura")
        print("6. Eliminar asignatura")
        print("7. Asignar asignatura a alumno")
        print("8. Descargar notas de alumno")
        print("9. Listar alumnos")
        print("10. Listar asignaturas")
        print("11. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_alumno(repo_alumnos)
        elif opcion == "2":
            modificar_alumno(repo_alumnos)
        elif opcion == "3":
            rut = input("RUT del alumno a eliminar: ")
            repo_alumnos.eliminar(rut)
        elif opcion == "4":
            crear_asignatura(repo_asig)
        elif opcion == "5":
            modificar_asignatura(repo_asig)
        elif opcion == "6":
            codigo = input("Código de la asignatura a eliminar: ")
            repo_asig.eliminar(codigo)
        elif opcion == "7":
            asignar_asignatura_alumno(repo_alumnos, repo_asig)
        elif opcion == "8":
            descargar_notas(repo_alumnos)
        elif opcion == "9":
            if repo_alumnos.alumnos:
                for a in repo_alumnos.alumnos.values():
                    print(f"{a.rut} - {a.nombre} ({a.roles()})")
            else:
                print("No hay alumnos registrados.")
        elif opcion == "10":
            if repo_asig.asignaturas:
                for a in repo_asig.asignaturas.values():
                    print(a)
            else:
                print("No hay asignaturas registradas.")
        elif opcion == "11":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
