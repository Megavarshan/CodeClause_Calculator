import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 18), bd=10, insertwidth=4,
                              width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('.', 5, 0), ('DEL', 5, 1)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=('Helvetica', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=10, pady=10)

    def on_button_click(self, value):
        if value == 'C':
            self.result_var.set("0")
        elif value == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid expression")
                self.result_var.set("0")
        elif value == 'DEL':
            current_value = self.result_var.get()
            if current_value != "0":
                new_value = current_value[:-1]
                self.result_var.set(new_value if new_value != "" else "0")
        else:
            current_value = self.result_var.get()
            if current_value == "0" or current_value == "Error":
                self.result_var.set(value)
            else:
                self.result_var.set(current_value + value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
