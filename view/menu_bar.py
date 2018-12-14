import tkinter as tk

from controller import files as controller


class MenuBar(tk.Menu):
    def _open(self):
        print('Open')

    def _save(self):
        print('save')

    def _export(self):
        print('export')

    def _undo(self):
        print('undo')

    def _redo(self):
        print('redo')

    def _bgnd_blank(self):
        self.editor.edit_canvas.set_blank()

    def _bgnd_bat(self):
        self.editor.edit_canvas.set_battle()

    def _bgnd_grid(self):
        self.editor.edit_canvas.set_grid()

    def _bgnd_bgrid(self):
        self.editor.edit_canvas.set_battle_grid()

    def __init__(self, root):
        tk.Menu.__init__(self, root)
        self.editor = None

        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu.add_command(label="New", command=controller.new_anim)
        self.file_menu.add_command(label="Open", command=controller.open_anim)
        self.file_menu.add_command(label="Save", command=controller.save)
        self.file_menu.add_command(label="Save as", command=controller.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Preview", command=self._export)
        self.file_menu.add_command(label="Export", command=self._export)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self._undo)
        self.edit_menu.add_command(label="Redo", command=self._redo)
        self.add_cascade(label="Edit", menu=self.edit_menu)

        self.bgnd_menu = tk.Menu(self, tearoff=0)
        self.bgnd_menu.add_command(label="Blank", command=self._bgnd_blank)
        self.bgnd_menu.add_command(label="Battle Template", command=self._bgnd_bat)
        self.bgnd_menu.add_command(label="Grid", command=self._bgnd_grid)
        self.bgnd_menu.add_command(label="Battle Template Grid", command=self._bgnd_bgrid)
        self.add_cascade(label="Background", menu=self.bgnd_menu)

        root.configure(menu=self)

    def set_edtitor(self, e):
        self.editor = e
