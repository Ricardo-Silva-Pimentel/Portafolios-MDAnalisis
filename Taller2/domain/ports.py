from abc import ABC, abstractmethod

class RepositorioPagoPort(ABC):
    @abstractmethod
    def guardar(self, pago):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def buscar_por_cliente(self, nombre_cliente):
        pass

    @abstractmethod
    def buscar_por_id(self, id_pago):
        pass

    @abstractmethod
    def eliminar(self, id_pago):
        pass
