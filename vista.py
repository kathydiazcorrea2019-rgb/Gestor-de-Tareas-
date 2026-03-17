import tkinter as tk
from tkinter import ttk


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x450")
        self.root.configure(bg="#f8f0f2")

# Estilo de la vista
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Titulo.TLabel",
                        font=("Segoe UI", 18, "bold"),
                        foreground="#5a189a",
                        background="#f8f0f2")

        style.configure("Sub.TLabel",
                        font=("Segoe UI", 10),
                        background="#f8f0f2")

        style.configure("Boton.TButton",
                        font=("Segoe UI", 11, "bold"),
                        padding=8,
                        foreground="white",
                        background="#c77dff")

        style.map("Boton.TButton",
                  background=[("active", "#9d4edd")])

        style.configure("Card.TFrame",
                        background="#ffffff",
                        relief="flat")

        # ---------- CONTENEDOR PRINCIPAL ----------
        self.card = ttk.Frame(root, style="Card.TFrame")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=450, height=420)

#        
        self.label = ttk.Label(self.card, text="Mis Tareas 📝", style="Titulo.TLabel")
        self.label.pack(pady=(15, 5))

        self.sub = ttk.Label(self.card, text="Organiza tu día de forma bonita 💖", style="Sub.TLabel")
        self.sub.pack(pady=(0, 15))

        # ---------- INPUT ----------
        self.entry = ttk.Entry(self.card, width=30)
        self.entry.pack(pady=5, ipady=5)

        # ---------- BOTONES ----------
        self.boton_agregar = ttk.Button(self.card, text="Agregar", style="Boton.TButton")
        self.boton_agregar.pack(pady=10)

        # ---------- LISTA ----------
        self.listbox = tk.Listbox(
            self.card,
            width=35,
            height=8,
            bg="#fff0f6",
            fg="#3c096c",
            font=("Segoe UI", 10),
            bd=0,
            highlightthickness=0
        )
        self.listbox.pack(pady=10)

        # ---------- BOTÓN ELIMINAR ----------
        self.boton_eliminar = ttk.Button(self.card, text="Eliminar", style="Boton.TButton")
        self.boton_eliminar.pack(pady=5)
