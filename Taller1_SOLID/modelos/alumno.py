from abc import ABC, abstractmethod

class Alumno(ABC):
    def __init__(self, nombre, edad, rut, fecha_nacimiento):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def descargar_notas(self):
        print(f"Notas de {self.nombre}:")
        for asig in self.asignaturas:
            print(f"- {asig.nombre}: 7.0 (simulado)")

    @abstractmethod
    def roles(self):
        pass
