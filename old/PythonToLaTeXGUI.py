import tkinter as tk
from PythonToLaTeX import convert_to_latex


class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Converter")

        self.input_label = tk.Label(root, text="Enter math expression:")
        self.input_label.pack()

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.output_label = tk.Label(root, text="LaTeX expression:")
        self.output_label.pack()

        self.output_text = tk.Text(root, width=50, height=10)
        self.output_text.pack()

    def convert(self):
        input_expression = self.input_entry.get()
        latex_expression = convert_to_latex(input_expression)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, latex_expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()