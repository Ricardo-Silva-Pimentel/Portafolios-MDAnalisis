from domain.ports import RepositorioPagoPort

class RepositorioPagoMemoria(RepositorioPagoPort):
    def __init__(self):
        self.pagos = {}

    def guardar(self, pago):
        self.pagos[pago.id] = pago

    def listar(self):
        return list(self.pagos.values())

    def buscar_por_cliente(self, nombre_cliente):
        return [p for p in self.pagos.values() if p.nombre_cliente.lower() == nombre_cliente.lower()]

    def buscar_por_id(self, id_pago):
        return self.pagos.get(id_pago)

    def eliminar(self, id_pago):
        if id_pago in self.pagos:
            del self.pagos[id_pago]
