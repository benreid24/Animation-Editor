import tkinter as tk

from .edit_canvas import EditCanvas
from .menu_bar import MenuBar
from .controls import Controls
from .images_list import ImageList


class AnimationEditor:
    def __init__(self):
        self.TK_ROOT = tk.Tk()
        self.TK_ROOT.title('Animation Editor')
        self.TK_ROOT.resizable(False, False)

        self.menu_bar = MenuBar(self.TK_ROOT)
        self.edit_canvas = EditCanvas(self.TK_ROOT)
        self.controls = Controls(self.TK_ROOT)
        self.image_list = ImageList(self.TK_ROOT)

    def mainloop(self):
        self.TK_ROOT.mainloop()
