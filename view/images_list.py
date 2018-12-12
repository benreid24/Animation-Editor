import tkinter as tk
from PIL import ImageTk, Image


class ImageList(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Images')

        self.button_frame = tk.Frame(self)
        self.add_but = tk.Button(self.button_frame, text='Add', command=self.add)
        self.delete_but = tk.Button(self.button_frame, text='Delete', command=self.delete)
        self.vert_but = tk.Button(self.button_frame, text='Clone via Vertical Flip', command=self.vert_clone)
        self.hori_but = tk.Button(self.button_frame, text='Clone via Horizontal Flip', command=self.hori_clone)
        self.add_but.grid(row=0, column=0, pady=5)
        self.delete_but.grid(row=0, column=1, pady=5)
        self.vert_but.grid(row=0, column=2, pady=5)
        self.hori_but.grid(row=0, column=3, pady=5)
        self.button_frame.pack(side='top')

        self.list_frame = tk.Frame(self)
        self.images_list = tk.Canvas(self.list_frame)
        self.scrollbar = tk.Scrollbar(self.list_frame, orient='horizontal', command=self.images_list.xview)

        self.selected_image = tk.IntVar()
        self.img = ImageTk.PhotoImage(Image.open('radio.png').resize((100, 100)))
        for i in range(0, 20):
            radio = tk.Radiobutton(self, image=self.img, value=i, variable=self.selected_image)
            self.images_list.create_window(i*120, 0, window=radio, width=120, height=120)
        self.images_list.configure(scrollregion=self.images_list.bbox('all'), xscrollcommand=self.scrollbar.set)
        self.images_list.pack(fill='both', expand=True, side='top')
        self.scrollbar.pack(fill='both', expand=True, side='bottom')
        self.list_frame.pack(fill='both', expand=True, side='bottom')

        self.grid(row=1, column=0, sticky=tk.W+tk.E)

    def add(self):
        print('add')

    def delete(self):
        print('delete')

    def vert_clone(self):
        print('vert')

    def hori_clone(self):
        print('hori')
