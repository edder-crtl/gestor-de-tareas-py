###imports
import datetime
from funciones import confirmacion, pedir_fecha, mostrar_estados
from clases_usuario import Tarea
from datos import Tareas, ESTADOS





def mostrar_tarea(lista):
    if not lista:
        print('No hay tareas registradas.')
    else:
        for i,p in enumerate(lista,start=1):
            print(f'{i}. nombre de la tarea:{p.titulo} \n descripcion de la tarea: {p.descripcion} \n fecha de creacion de la tarea: {p.fecha_creacion} \n fecha de entrega: {p.fecha_entrega}, \n estado de la tarea: {ESTADOS.get(p.estado,'desconocido \n ')}')



def crear_tarea(lista):
    while True:
        try:
            titulo= input('ingrese el titulo de la tarea:')
            if titulo=='':
                print('el titulo no puede estar vacio')
                confirmacion()
                continue
            descripcion = input('ingrese la descripcion de la tarea: ')
            if descripcion=='':
                print('la descripcion no puede estar vacia')
                confirmacion()
                continue
            fecha_creacion= datetime.datetime.now()
            fecha_entrega=pedir_fecha()
            estado=1
        except ValueError:
            print('tipo de dato erroneo, asegurese de llenarlo bien')

        nueva=Tarea(
            titulo=titulo,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            fecha_entrega=fecha_entrega,
            estado=estado,
        )

        lista.append(nueva)
        break



def modifcar_tarea_externa(lista):
    while True:
        mostrar_tarea(lista)
        try:
            indice=int(input('selecione la tarea a modificar: '))
            indice=indice-1
            if indice<0 or indice>=len(lista):
                print('usurio inexistente, ingrese uno valido.')
                confirmacion()
                continue
            tarea_selecionada=lista[indice]
            modifcar_tarea_interna(lista, tarea_selecionada)
            break
        except ValueError:
            print('tipo de dato erroneo, ingrese un numero de usuario correcto')
            confirmacion()
            continue


def modifcar_tarea_interna(lista, tarea_selecionada):
    while True:
        try:
            opcion=int(input('''\nselecione la opcion que desea modificar del usuario:
0. salir del menu
1. titulo 
2. descripcion
3. estado
'''))
        except ValueError:
            print('tipo de dato erroneo, compruebe que esta usando un numero')

        if opcion==0:
            print('cambios guardados con exito, hasta pronto.')
            break

        elif opcion==1:
            while True:
                nuevo_nombre=input('ingrese el nuevo titulo: ')
                if nuevo_nombre=='':
                    print("el titulo no puede estar vacio, intentelo nuevamente.")
                    continue
                tarea_selecionada.titulo=nuevo_nombre
                print('actualizada con exito')
                confirmacion()
                break

        elif opcion==2:
            while True:
                nueva_descripcion=input('ingrese la nueva descripcion: ')
                if nueva_descripcion=='':
                    print('la descripcion no puede estar vacia, reintenelo.')
                    confirmacion()
                    continue
                tarea_selecionada.descripcion=nueva_descripcion
                print('actualizada con exito')
                confirmacion()
                break

        elif opcion==3:
            while True:
                mostrar_estados()
                try:
                    nuevo_estado=int(input('selecione su opcion: '))
                    if nuevo_estado not in ESTADOS:
                        print('estado inexistente, ingrese uno correcto.')
                        confirmacion()
                        continue
                    tarea_selecionada.estado=nuevo_estado
                    print('actualizada con exito.')
                    confirmacion()
                    break
                except ValueError:
                    print('tipo de dato incorrecto, ingrese uno valido')


def selecionar_borrar_tarea(lista):
    mostrar_tarea()
    while True:
        try:
            opcion=int(input('Selecion el usuario a eliminar: '))
            indice=opcion-1
            if indice <0 or indice >=len(lista):
                print('usuario inexistente, ingrese uno valido')
                confirmacion()
                continue
            borrar_tarea(lista, indice)
            print('borrado con exito')
            break
        except ValueError:
            print('tipo de dato invalido, ingrese un numero')
            confirmacion()
            continue



def borrar_tarea(lista, indice):
    lista.pop(indice)