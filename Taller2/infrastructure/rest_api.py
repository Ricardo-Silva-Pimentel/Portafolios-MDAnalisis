from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from application.services import ServicioPago
from infrastructure.repositories import RepositorioPagoMemoria

app = FastAPI()
repo = RepositorioPagoMemoria()
servicio = ServicioPago(repo)

class PagoOut(BaseModel):
    id: str
    nombre_cliente: str
    monto: float
    fecha: datetime
    estado: str

@app.post("/pagos", status_code=201, response_model=PagoOut)
def registrar_pago(data: dict):
    try:
        pago = servicio.registrar_pago(data["nombre_cliente"], data["monto"])
        return PagoOut(**vars(pago))
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/pagos", response_model=list[PagoOut])
def listar_pagos():
    return [PagoOut(**vars(p)) for p in servicio.listar_pagos()]

@app.get("/pagos/cliente/{nombre_cliente}", response_model=list[PagoOut])
def buscar_pagos(nombre_cliente: str):
    return [PagoOut(**vars(p)) for p in servicio.buscar_pagos_por_cliente(nombre_cliente)]

@app.delete("/pagos/{id_pago}", status_code=204)
def eliminar_pago(id_pago: str):
    exito, mensaje = servicio.eliminar_pago(id_pago)
    if exito:
        return
    raise HTTPException(status_code=400, detail=mensaje)
