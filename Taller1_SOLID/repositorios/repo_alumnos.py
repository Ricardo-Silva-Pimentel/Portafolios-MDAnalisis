class RepositorioAlumnos:
    def __init__(self):
        self.alumnos = {}

    def crear(self, alumno):
        self.alumnos[alumno.rut] = alumno
        print(f"Alumno {alumno.nombre} creado (simulado).")

    def recuperar(self, rut):
        return self.alumnos.get(rut, None)

    def modificar(self, rut, alumno_nuevo):
        if rut in self.alumnos:
            self.alumnos[rut] = alumno_nuevo
            print(f"Alumno {rut} modificado (simulado).")
        else:
            print("Alumno no encontrado.")

    def eliminar(self, rut):
        if rut in self.alumnos:
            del self.alumnos[rut]
            print(f"Alumno {rut} eliminado (simulado).")
        else:
            print("Alumno no encontrado.")
