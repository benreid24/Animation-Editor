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

        self.edit_menu = tk.Menu(self, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.add_cascade(label="Edit", menu=self.edit_menu)

        self.bgnd_menu = tk.Menu(self, tearoff=0)
        self.bgnd_menu.add_command(label="Blank", command=self.bgnd_blank)
        self.bgnd_menu.add_command(label="Battle Template", command=self.bgnd_bat)
        self.bgnd_menu.add_command(label="Grid", command=self.bgnd_grid)
        self.bgnd_menu.add_command(label="Battle Template Grid", command=self.bgnd_bgrid)
        self.add_cascade(label="Background", menu=self.bgnd_menu)

        root.configure(menu=self)

    def create(self):
        print('create')

    def open(self):
        print('Open')

    def save(self):
        print('save')

    def export(self):
        print('export')

    def undo(self):
        print('undo')

    def redo(self):
        print('redo')

    def bgnd_blank(self):
        print('blank')

    def bgnd_bat(self):
        print('battle')

    def bgnd_grid(self):
        print('grid')

    def bgnd_bgrid(self):
        print('bgrid')
