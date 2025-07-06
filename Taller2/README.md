# Taller 2: Arquitectura Hexagonal y REST

Este proyecto implementa un sistema de gestión de pagos utilizando arquitectura hexagonal y una API REST con FastAPI.

## Descripción

El sistema permite gestionar pagos de clientes a través de una API REST. La lógica está separada en dominio, aplicación y adaptadores siguiendo el modelo de arquitectura hexagonal. Los datos se almacenan en memoria y se pierden al reiniciar el servidor.

## Funcionalidades

- Registrar un pago (nombre del cliente, monto).
- Listar todos los pagos.
- Buscar pagos por nombre de cliente.
- Eliminar un pago por su ID si su estado es COMPLETADO.

## Supuestos

- Todos los datos se almacenan en un repositorio en memoria.
- Los pagos tienen estado COMPLETADO al ser registrados.
- El monto debe ser mayor que cero para ser válido.
- No se valida el nombre del cliente, se acepta cualquier texto.
- No hay autenticación ni autorización en el sistema.

## Estructura del sistema

- **Dominio:** clase `Pago` (entidad) y puerto `RepositorioPagoPort` (interfaz del repositorio).
- **Aplicación:** clase `ServicioPago` (casos de uso).
- **Infraestructura:** implementación en memoria del repositorio y el adaptador REST (FastAPI).
- **Entry point:** `main.py` para iniciar la API.

## Cómo ejecutar

1. Instalar las dependencias:

   pip install fastapi uvicorn


2. Iniciar el servidor:

   python -m uvicorn main:app --reload


3. Acceder a la documentación interactiva:

   http://127.0.0.1:8000/docs


## Endpoints

- **POST /pagos**
  - Registra un pago.
  - Requiere: nombre_cliente (str), monto (float > 0).

- **GET /pagos**
  - Devuelve todos los pagos registrados.

- **GET /pagos/cliente/{nombre_cliente}**
  - Devuelve los pagos de un cliente específico.

- **DELETE /pagos/{id_pago}**
  - Elimina un pago si está en estado COMPLETADO.


## Acceso:
El repositorio incluye acceso para el colaborador @MrNeo44.
