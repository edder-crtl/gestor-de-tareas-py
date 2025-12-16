### imports
from funciones import confirmacion, guardar_tareas
from crud import crear_tarea, modifcar_tarea_externa, mostrar_tarea, borrar_tarea
from datos import Tareas

###menu principal
while True:
    try:
        print('''\n bienvenido a su gestor de tareas:\n
0. salir
1. crear tarea
2. mostrar tarea
3. modificar tarea 
4. eliminar tarea
''')
        opcion=int(input('\n selecione su opcion: '))
    except ValueError:
            print('ingrese un valor correcto')
            confirmacion()
            continue

    if opcion==0:
        guardar_tareas(Tareas)
        print('Salida con exito, feliz dia')
        break
    elif opcion==1:
        crear_tarea(Tareas)
        guardar_tareas(Tareas)
        confirmacion()
    elif opcion==2:
        mostrar_tarea(Tareas)
        guardar_tareas(Tareas)
        confirmacion()
    elif opcion==3:
        modifcar_tarea_externa(Tareas)
        guardar_tareas(Tareas)
        confirmacion()
    elif opcion==4:
        borrar_tarea(Tareas)
        guardar_tareas(Tareas)
        confirmacion()

    else:
        print('opcion invalida vuelve a intentarlo')


