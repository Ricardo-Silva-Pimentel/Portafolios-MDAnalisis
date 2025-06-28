class Asignatura:
    def __init__(self, nombre, codigo, creditos, tipo):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = tipo # tipo puede ser "pregrado", "magister", "doctorado" o "general"

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.creditos} créditos) [{self.tipo}]"
