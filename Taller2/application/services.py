from domain.models import Pago

class ServicioPago:
    def __init__(self, repo):
        self.repo = repo

    def registrar_pago(self, nombre_cliente, monto):
        pago = Pago(nombre_cliente, monto)
        self.repo.guardar(pago)
        return pago

    def listar_pagos(self):
        return self.repo.listar()

    def buscar_pagos_por_cliente(self, nombre_cliente):
        return self.repo.buscar_por_cliente(nombre_cliente)

    def eliminar_pago(self, id_pago):
        pago = self.repo.buscar_por_id(id_pago)
        if not pago:
            return False, "Pago no encontrado."
        if pago.estado != "COMPLETADO":
            return False, "El pago no se puede eliminar, estado inválido."
        self.repo.eliminar(id_pago)
        return True, ""
