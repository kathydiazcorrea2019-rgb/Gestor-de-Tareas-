# Sistema de Gestión de Tareas

## Descripción

Este proyecto consiste en una aplicación desarrollada en Python que permite gestionar una lista de tareas (To-Do List).  
Las tareas se almacenan en un archivo de texto llamado `tareas.txt`.

El programa fue desarrollado utilizando Programación Orientada a Objetos y una arquitectura basada en Modelo-Vista-Controlador (MVC).

---

## Funcionalidades

- Agregar nuevas tareas
- Mostrar todas las tareas almacenadas
- Eliminar tareas (marcarlas como completadas)
- Interfaz gráfica amigable con Tkinter

---

## Estructura del Proyecto

- **modelo.py:** Maneja el acceso al archivo y la lógica de datos
- **vista.py:** Interfaz gráfica del usuario
- **controlador.py:** Conecta la vista con el modelo
- **main.py:** Punto de inicio del programa

---

## Explicación

El sistema está dividido en tres partes:

- **Modelo:** Se encarga de guardar, leer y eliminar tareas del archivo
- **Vista:** Muestra la interfaz gráfica
- **Controlador:** Gestiona la lógica del programa y conecta todo

Esto permite que el código sea más organizado y fácil de mantener.

---

## Ejemplo de uso

Entrada:
Agregar tarea → "Hacer tarea de programación"

Salida:
La tarea aparece en la lista

Eliminar tarea:
Se elimina de la lista y del archivo

---

## Autor

Kathy Diaz Correa
