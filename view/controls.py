import tkinter as tk

from .frame_options import FrameOptions
from .piece_settings import PieceSettings
from .frame_list import FrameList


class Controls(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.frame_options = FrameOptions(self)
        self.piece_settings = PieceSettings(self)
        self.frame_list = FrameList(self)

        self.grid(column=1, row=0, sticky=tk.W+tk.E+tk.N+tk.S)
