import tkinter as tk


class PieceSettings(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Image Options', padx=3, pady=3)

        self.clone_but = tk.Button(self, text='Clone', command=self.clone)
        self.delete_but = tk.Button(self, text='Delete', command=self.clone)
        self.update_but = tk.Button(self, text='Update', command=self.set)
        self.clone_but.grid(row=0, column=0, pady=5)
        self.delete_but.grid(row=0, column=1, pady=5)
        self.update_but.grid(row=0, column=2, pady=5)

        self.xpos_label = tk.Label(self, text='X Pos:')
        self.xpos_entry = tk.Entry(self)
        self.xpos_label.grid(row=1, column=0)
        self.xpos_entry.grid(row=1, column=1)
        self.ypos_label = tk.Label(self, text='Y Pos:')
        self.ypos_entry = tk.Entry(self)
        self.ypos_label.grid(row=1, column=2)
        self.ypos_entry.grid(row=1, column=3)

        self.xscale_entry = tk.Scale(self, from_=0, to=1000, resolution=1, orient=tk.VERTICAL, label='X Scale %')
        self.xscale_entry.set(100)
        self.xscale_entry.grid(row=2, column=0, rowspan=2)
        self.yscale_entry = tk.Scale(self, from_=0, to=1000, resolution=1, orient=tk.VERTICAL, label='Y Scale %')
        self.yscale_entry.set(100)
        self.yscale_entry.grid(row=2, column=1, rowspan=2)
        self.rotation_entry = tk.Scale(self, from_=0, to=360, resolution=1, orient=tk.HORIZONTAL, label='Rotation')
        self.rotation_entry.set(0)
        self.rotation_entry.grid(row=2, column=2, columnspan=2)
        self.trans_entry = tk.Scale(self, from_=0, to=256, resolution=1, orient=tk.HORIZONTAL, label='Opacity')
        self.trans_entry.set(256)
        self.trans_entry.grid(row=3, column=2, columnspan=2)

        self.grid(row=1, column=0, columnspan=2)

    def clone(self):
        print('clone')

    def set(self):
        print('update')
