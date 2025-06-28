class RepositorioAsignaturas:
    def __init__(self):
        self.asignaturas = {}

    def crear(self, asignatura):
        self.asignaturas[asignatura.codigo] = asignatura
        print(f"Asignatura {asignatura.nombre} creada (simulado).")

    def recuperar(self, codigo):
        return self.asignaturas.get(codigo, None)

    def modificar(self, codigo, asignatura_nueva):
        if codigo in self.asignaturas:
            self.asignaturas[codigo] = asignatura_nueva
            print(f"Asignatura {codigo} modificada (simulado).")
        else:
            print("Asignatura no encontrada.")

    def eliminar(self, codigo):
        if codigo in self.asignaturas:
            del self.asignaturas[codigo]
            print(f"Asignatura {codigo} eliminada (simulado).")
        else:
            print("Asignatura no encontrada.")
