from modelos.alumno import Alumno


class Titulado(Alumno):
    def roles(self):
        return "No estudia, no hace ayudantías."

class EstudianteNoAyudante(Alumno):
    def roles(self):
        return "Estudia."

class EstudianteAyudante(Alumno):
    def roles(self):
        return "Estudia y hace ayudantías."

class EstudianteMagister(Alumno):
    def roles(self):
        return "Estudia y hace clases."

class EstudianteDoctorado(Alumno):
    def roles(self):
        return "Estudia, hace clases e investiga."
