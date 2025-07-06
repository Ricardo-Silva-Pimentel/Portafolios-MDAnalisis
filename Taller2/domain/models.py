from datetime import datetime
import uuid

class Pago:
    def __init__(self, nombre_cliente, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        self.id = str(uuid.uuid4())
        self.nombre_cliente = nombre_cliente
        self.monto = monto
        self.fecha = datetime.now()
        self.estado = "COMPLETADO"
