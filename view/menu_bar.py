import tkinter as tk


class MenuBar(tk.Menu):
    def __init__(self, root):
        tk.Menu.__init__(self, root)

        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu.add_command(label="New", command=self.create)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(label="Export", command=self.export)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.add_cascade(label="File", menu=self.file_menu)

        root.configure(menu=self)

    def create(self):
        print('create')

    def open(self):
        print('Open')

    def save(self):
        print('save')

    def export(self):
        print('export')
