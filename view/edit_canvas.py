import tkinter as tk


class EditCanvas(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bd=2)

        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.grid()
        self.canvas.create_rectangle(0, 0, 800, 600, fill='red')
        self.canvas.create_rectangle(50, 50, 100, 100, fill='blue')

        self.grid(row=0, column=0)
