import datetime
from dataclasses import dataclass

####dataclass
@dataclass
class Tarea:
    titulo: str
    descripcion: str
    fecha_creacion: datetime.datetime
    fecha_entrega: datetime.datetime
    estado: int 
