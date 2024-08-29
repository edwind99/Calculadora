import tkinter as tk
from tkinter import font
import util.util_ventana as util_ventana
from config import constantes as cons


class FormularioCalculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widget()
        self.construir_widget_toggle()

    def config_window(self):
        # Configuración de la ventana
        self.title('Python GUI Calculadora')
        # Config color de fondo y hacer transparente la ventana
        self.configure(bg=cons.FONDO_DARK)
        self.attributes('-alpha', 0.96)
        w, h = 370, 570
        util_ventana.centrar_ventana(self, w, h)

    def construir_widget(self):
        # Etiqueta pa mostrar la operación solicitada
        self.operation_label = tk.Label(self, text="", font=(
            'Arial', 16), fg=cons.TEXTO_DARK, bg=cons.FONDO_DARK, justify='right')
        self.operation_label.grid(
            row=0, column=3, padx=10, pady=10)  # columnspan

        # pantalla de operacion
        self.entry = tk.Entry(self, width=12, font=(
            'Arial', 40), bd=1, fg=cons.TEXTO_DARK, bg=cons.CAJA_TEXTO_DARK, justify='right')
        self.entry.grid(row=1, column=0, columnspan=4,
                        padx=10, pady=10)  # padding

        # botones
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row_val = 2
        col_val = 0

        # tipografia de los botones
        roboto_font = font.Font(family="Roboto", size=16)

        for button in buttons:
            # color de fondo para los otros botones
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.BOTONES_ESPECIALES_DARK
                # tamaño de los botones
                button_font = font.Font(size=16, weight='bold')
            else:
                color_fondo = cons.BOTONES_DARK
                button_font = roboto_font

            if button == '=':
                tk.Button(self, text=button, width=11, height=2, command=lambda b=button: self.on_button_click(b),
                          bg=color_fondo, fg=cons.TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0,
                          overrelief='flat').grid(row=row_val, column=col_val, columnspan=2, pady=5)  # columnspan
                col_val += 1
            else:
                tk.Button(self, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b),
                          bg=color_fondo, fg=cons.TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0,
                          overrelief='flat').grid(row=row_val, column=col_val, pady=5)  # padding
                col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

    def construir_widget_toggle(self):
        # Iniciar con el tema oscuro
        self.dark_theme = True
       
    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/100')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                # Mostrar la operación en la etiqueta sin =
                operation = expression + " " + value
                self.operation_label.config(text=operation)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")
        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")
        elif value == '<':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]  # eliminar el último caracter
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
                # actualizar la etiqueta de operación
                self.operation_label.config(text=new_text + " ")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            # actualizar la etiqueta de operación solo cuando se presiona '='
            if value == '=':
                self.operation_label.config(text="")