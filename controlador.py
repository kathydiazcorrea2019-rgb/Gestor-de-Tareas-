from modelo import GestorTareas
from tkinter import messagebox


class Controlador:
    def __init__(self, vista):
#se conecta la vista con el modelo
        self.vista = vista
        self.modelo = GestorTareas()

# conectar botones con funciones
        self.vista.boton_agregar.config(command=self.agregar_tarea)
        self.vista.boton_eliminar.config(command=self.eliminar_tarea)
# se cargan las tareas al iniciar el programa
        self.cargar_tareas()

    def cargar_tareas(self):
# limpiar la vista antes de cargar
        self.vista.listbox.delete(0, "end")
 # obtener tareas desde el archivo
        tareas = self.modelo.obtener_tareas()
# insertar en la Interfaz
        for tarea in tareas:
            self.vista.listbox.insert("end", tarea)

    def agregar_tarea(self):
# Obtener texto del campo de entrada
        tarea = self.vista.entry.get().strip()
# verificar que no este vacio 
        if tarea == "":
            messagebox.showwarning("Error", "La tarea no puede estar vacía.")
            return
# guardar tarea en el archivo
        self.modelo.agregar_tarea(tarea)
# Limpiar el campo de entrada    
        self.vista.entry.delete(0, "end")
# Actualizar la lista
        self.cargar_tareas()

    def eliminar_tarea(self):
# Obtener tarea seleccionada
        seleccion = self.vista.listbox.curselection()

# Verificar seleccion 
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona una tarea.")
            return

# Obtener indice y texto de la tarea
        indice = seleccion[0]
        tarea = self.vista.listbox.get(indice)

# Eliminar del archivo
        self.modelo.eliminar_tarea(tarea)
# Actualizar la lista
        self.cargar_tareas()
