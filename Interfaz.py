#Alumna: Mirelena Francisca Mindiola Gouriyu
#Fecha de Realizacion del programa: 26 de Mayo del 2024

#Descripcion: Diseño y implementacion de la Interfaz

#Paquetes utilizados
import tkinter as tk
from tkinter import messagebox
from matrix_operations import *

#Creacion de la clase principal para la Aplicacion
class MatrixOperationsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("MatrizApp")
        self.create_widgets()
#
    def create_widgets(self):
        #Creacion de la Descripcion
        self.label_description = tk.Label(self.master, text="Bienvenido(a),Esta aplicación permite realizar operaciones con matrices. "
                                                           "Por favor, introduzca las Filas y Columnas luego presione el boton para la creacion de la matriz "
                                                           ,
                                          wraplength=400, justify="left")
        self.label_description.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#Creacion Filas
        self.label_rows = tk.Label(self.master, text="Número de filas:")
        self.label_rows.grid(row=1, column=0, padx=10, pady=5)
        self.entry_rows = tk.Entry(self.master)
        self.entry_rows.grid(row=1, column=1, padx=10, pady=5)
        
#Creacion de Columnas
        self.label_cols = tk.Label(self.master, text="Número de columnas:")
        self.label_cols.grid(row=2, column=0, padx=10, pady=5)
        self.entry_cols = tk.Entry(self.master)
        self.entry_cols.grid(row=2, column=1, padx=10, pady=5)
        
#Boton
        self.button_create_matrix = tk.Button(self.master, text="Crear Matriz", command=self.create_matrix)
        self.button_create_matrix.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

#Creacion de la matriz
    def create_matrix(self):
        try:
            self.rows = int(self.entry_rows.get())
            self.cols = int(self.entry_cols.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos para filas y columnas.")
            return
        
        self.matrix = []

        self.matrix_window = tk.Toplevel(self.master)
        self.matrix_window.title("Ingrese los elementos de la matriz")

        label_description = tk.Label(self.matrix_window, text="Ingrese los elementos de la matriz en los campos a continuación.",
                                     wraplength=400, justify="left")
        label_description.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)

        self.entries = []
        for i in range(self.rows):
            row_entries = []
            for j in range(self.cols):
                entry = tk.Entry(self.matrix_window, width=5)
                entry.grid(row=i+1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        button_done = tk.Button(self.matrix_window, text="Hecho", command=self.process_matrix)
        button_done.grid(row=self.rows+1, columnspan=self.cols, padx=10, pady=5)
        
#Procesamiento de la matriz Ingresada
    def process_matrix(self):
        try:
            self.matrix_values = []
            for i in range(self.rows):
                row_values = []
                for j in range(self.cols):
                    value = int(self.entries[i][j].get())
                    row_values.append(value)
                self.matrix_values.append(row_values)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos para los elementos de la matriz.")
            return

        self.matrix_window.destroy()  # Cerrar la ventana después de crear la matriz

        self.operation_window = tk.Toplevel(self.master)
        self.operation_window.title("Seleccione la operación")

        operations = ["Suma", "Resta", "Multiplicación por Escalar", "Multiplicación de Matrices"]
        self.selected_operation = tk.StringVar()

        # Añadir texto
        label_matrix_text = tk.Label(self.operation_window, text="Elementos de la matriz:")
        label_matrix_text.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=5)

        # Mostrar los elementos de la matriz ingresada centrados
        num_rows = len(self.matrix_values)
        num_cols = len(self.matrix_values[0])
        for i in range(num_rows):
            for j in range(num_cols):
                label = tk.Label(self.operation_window, text=str(self.matrix_values[i][j]))
                label.grid(row=i+1, column=j+1, padx=5, pady=5, sticky="nsew")
        
        # Centrar la matriz en la ventana
        for i in range(num_rows + 1):
            self.operation_window.grid_rowconfigure(i, weight=1)
        for i in range(num_cols + 1):
            self.operation_window.grid_columnconfigure(i, weight=1)

        # Añadir tipo de matriz
        label_matrix_type = tk.Label(self.operation_window, text=f"Tipo de matriz: {num_rows}x{num_cols}")
        label_matrix_type.grid(row=num_rows+2, column=0, columnspan=num_cols, padx=10, pady=5)

        # Añadir opciones debajo de la matriz
        for i, operation in enumerate(operations):
            rb = tk.Radiobutton(self.operation_window, text=operation, variable=self.selected_operation, value=operation)
            rb.grid(row=num_rows+3, column=i, padx=10, pady=5)

        button_execute = tk.Button(self.operation_window, text="Ejecutar", command=self.execute_operation)
        button_execute.grid(row=num_rows+4, columnspan=len(operations), padx=10, pady=5)

        #Ejecucion de las operaciones
    def execute_operation(self):
        operation = self.selected_operation.get()
        if operation == "Suma":
            self.get_second_matrix(add_matrices)
        elif operation == "Resta":
            self.get_second_matrix(subtract_matrices)
        elif operation == "Multiplicación por Escalar":
            self.get_scalar()  # Llama a la función para obtener el escalar
        elif operation == "Multiplicación de Matrices":
            self.get_second_matrix(multiply_matrices)
        else:
            messagebox.showerror("Error", "Operación no válida")


#Metodo Escalar
    def get_scalar(self):
        scalar_window = tk.Toplevel(self.master)
        scalar_window.title("Ingrese el escalar")

        label = tk.Label(scalar_window, text="Escalar:")
        label.grid(row=0, column=0, padx=10, pady=5)

        self.scalar_entry = tk.Entry(scalar_window)
        self.scalar_entry.grid(row=0, column=1, padx=10, pady=5)

        button_done = tk.Button(scalar_window, text="Hecho", command=lambda: self.process_scalar(scalar_window))
        button_done.grid(row=1, columnspan=2, padx=10, pady=5)
        
#Proceso del escalar
    def process_scalar(self, window):
        try:
            scalar = int(self.scalar_entry.get())
            result = multiply_matrix_scalar(self.matrix_values, scalar)
            self.display_result(result)
            window.destroy()  # Cierra la ventana después de procesar el escalar
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido para el escalar.")
            
#Agregar la segunda matriz
    def get_second_matrix(self, operation_func):
        # Obtiene la segunda matriz necesaria para algunas operaciones.
        second_matrix_window = tk.Toplevel(self.master)
        second_matrix_window.title("Ingrese los elementos de la segunda matriz")

        # Descripción de la segunda ventana para la segunda matriz
        label_description = tk.Label(second_matrix_window, text="Ingrese los elementos de la segunda matriz en los campos a continuación.",
                                     wraplength=400, justify="left")
        label_description.grid(row=0, column=0, columnspan=self.cols, padx=10, pady=10)

        self.second_entries = []
        for i in range(self.rows):
            row_entries = []
            for j in range(self.cols):
                entry = tk.Entry(second_matrix_window, width=5)
                entry.grid(row=i+1, column=j, padx=5, pady=5)  # Offset de fila por la descripción
                row_entries.append(entry)
            self.second_entries.append(row_entries)

        button_done = tk.Button(second_matrix_window, text="Hecho", command=lambda: self.process_second_matrix(operation_func, second_matrix_window))
        button_done.grid(row=self.rows+1, columnspan=self.cols, padx=10, pady=5)  # Offset de fila por la descripción

#Procesamiento de la segunda matriz
    def process_second_matrix(self, operation_func, window):
        # Procesa la segunda matriz ingresada por el usuario.
        try:
            second_matrix_values = []
            for i in range(self.rows):
                row_values = []
                for j in range(self.cols):
                    value = int(self.second_entries[i][j].get())
                    row_values.append(value)
                second_matrix_values.append(row_values)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos para los elementos de la matriz.")
            return

        window.destroy()
        result = operation_func(self.matrix_values, second_matrix_values)
        self.display_result(result)
        
#Resultado de la matriz 
    def display_result(self, result):
        # Muestra el resultado de la operación en una nueva ventana.
        result_window = tk.Toplevel(self.master)
        result_window.title("Resultado de la operación")

        for i, row in enumerate(result):
            for j, value in enumerate(row):
                label = tk.Label(result_window, text=str(value))
                label.grid(row=i, column=j, padx=5, pady=5)

        # Mostrar la descripción de la matriz resultante
        rows, cols = len(result), len(result[0])
        matrix_type = determine_matrix_type(result)
        description = f"Matriz de {rows}x{cols}\nTipo de matriz: {matrix_type}"
        description_label = tk.Label(result_window, text=description)
        description_label.grid(row=rows+1, column=0, columnspan=cols, padx=10, pady=10)


def main():
    # Inicia la aplicación.
    root = tk.Tk()
    app = MatrixOperationsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

