
####imports
import datetime
import json, os
from dataclasses import asdict
from clases_usuario import Tarea

### estados 

ESTADOS={
1:'PENDIENTE',
2:'EN PROGRESO',
3:'COMPLETADA'
}



###funciones



def guardar_tareas(lista):
    lista_dicts = []
    for t in lista:
        d = asdict(t)
        d["fecha_creacion"] = t.fecha_creacion.isoformat()
        d["fecha_entrega"] = t.fecha_entrega.isoformat()
        lista_dicts.append(d)

    with open("tareas.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_dicts, archivo, indent=4, ensure_ascii=False)


def cargar_tareas():
    if not os.path.exists("tareas.json"):
        return []

    with open("tareas.json", "r", encoding="utf-8") as archivo:
        lista_dicts = json.load(archivo)

    return [
        Tarea(
            d["titulo"],
            d["descripcion"],
            datetime.datetime.fromisoformat(d["fecha_creacion"]),
            datetime.datetime.fromisoformat(d["fecha_entrega"]),
            d["estado"]
        )
        for d in lista_dicts
    ]




def mostrar_estados():
    print('los estados disponibles son:')
    for i,estado in ESTADOS.items():
        print(f'{i}.{estado} ')

def confirmacion():
    input("Ingrese enter para continuar ")

def pedir_fecha():
    while True:
        fecha_str=input('ingrese la fecha (YYYY-MM-DD): ')
        try:
            fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha
        except ValueError:
            print('fecha invalida, use el formato YYYY-MM-DD:')


def historial_tareas():
    with open ('historial.json','a') as historial:
        json.dump()

