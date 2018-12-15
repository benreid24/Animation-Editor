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

        self.menu_bar.set_editor(self)

    def get_image_list(self):
        return self.image_list

    def get_main_canvas(self):
        return self.edit_canvas

    def get_piece_controls(self):
        return self.controls.piece_settings

    def get_frame_controls(self):
        return self.controls.frame_options

    def get_menu(self):
        return self.menu_bar

    def get_actions_panel(self):
        return self.controls.actions

    def get_interpolation_controls(self):
        return self.controls.interp_controls

    def mainloop(self):
        self.TK_ROOT.mainloop()
