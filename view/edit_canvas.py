import tkinter as tk
from .editable_piece import EditablePiece


class EditCanvas(tk.Frame):
    def _disable_all(self):
        for piece in self.pieces:
            piece.set_active(False)

    def __init__(self, master):
        tk.Frame.__init__(self, master, bd=2)

        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.grid()
        self.background = self.canvas.create_rectangle(0, 0, 800, 600, fill='red')
        self.canvas.tag_bind(self.background, '<Button-1>', self.check_click)

        self.pieces = [
            EditablePiece(self.canvas, 'radio.png', 200, 200)
        ]

        self.grid(row=0, column=0)
        # TODO bind event for b1 clicked. Check if not over any images. if not, set active image to inactive

    def check_click(self, event):
        items = self.canvas.find_overlapping(event.x, event.y, event.x+2, event.y+2)
        if len(items) <= 1:
            self._disable_all()
        else:
            for piece in self.pieces:
                if piece.contains(event.x, event.y):
                    piece.set_active(True)
                    break
