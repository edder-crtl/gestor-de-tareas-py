# Gestor de Tareas en Python

## Descripción general

Este proyecto es un gestor de tareas desarrollado en Python que implementa un CRUD completo (Crear, Leer, Actualizar y Eliminar) mediante una aplicación de consola. El objetivo principal es practicar fundamentos sólidos de programación estructurada y orientada a objetos, manteniendo una separación clara entre la lógica de negocio y la interacción con el usuario.

El sistema permite administrar tareas de forma persistente utilizando archivos JSON, garantizando que la información se conserve entre ejecuciones del programa.

---

## Características principales

* Creación de tareas con información estructurada
* Listado de tareas registradas
* Edición de tareas existentes
* Eliminación de tareas
* Persistencia automática de datos en archivos JSON
* Manejo de fechas mediante `datetime`
* Uso de `dataclasses` para modelar entidades
* Validación de entradas desde el menú
* Separación de responsabilidades (lógica vs interacción)

---

## Estructura del proyecto

El proyecto está organizado siguiendo un criterio de responsabilidades claras:

* **Menú / Interacción**

  * Muestra opciones al usuario
  * Solicita y valida entradas
  * Controla el flujo del programa
  * Decide cuándo persistir los cambios

* **Lógica de negocio (CRUD)**

  * Modifica los datos (crear, editar, eliminar)
  * No interactúa directamente con el usuario

* **Persistencia**

  * Conversión de objetos a diccionarios
  * Guardado y carga de datos desde JSON
  * Manejo explícito de tipos no serializables (fechas)

---

## Tecnologías y herramientas

* Python 3
* `dataclasses`
* `json`
* `datetime`
* Git y GitHub para control de versiones

---

## Funcionamiento general

1. Al iniciar el programa, las tareas se cargan automáticamente desde un archivo JSON si este existe.
2. El usuario interactúa con un menú en consola para seleccionar la operación deseada.
3. Las operaciones CRUD modifican la lista de tareas en memoria.
4. Después de cada operación que altera los datos, los cambios se guardan automáticamente.
5. Al cerrar el programa, la información permanece disponible para la siguiente ejecución.


---

## Autor

Proyecto desarrollado con fines educativos como parte del proceso de aprendizaje en desarrollo de software y buenas prácticas de programación.
