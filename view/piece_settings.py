import tkinter as tk


class PieceSettings(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Image Options', padx=3, pady=3)

        self.clone_but = tk.Button(self, text='Clone', command=self.clone)
        self.delete_but = tk.Button(self, text='Delete', command=self.clone)
        self.update_but = tk.Button(self, text='Update', command=self.apply, background='#ff5555')
        self.upbut = tk.Button(self, text='Move up', command=self.moveup)
        self.downbut = tk.Button(self, text='Move down', command=self.movedown)
        self.clone_but.grid(row=0, column=0, pady=5)
        self.delete_but.grid(row=0, column=1, pady=5)
        self.update_but.grid(row=0, column=2, pady=5)
        self.upbut.grid(row=0, column=3, pady=1)
        self.downbut.grid(row=1, column=3, pady=1)

        self.xpos_label = tk.Label(self, text='X Pos:')
        self.xpos_entry = tk.Entry(self)
        self.xpos_label.grid(row=2, column=0)
        self.xpos_entry.grid(row=3, column=0)
        self.ypos_label = tk.Label(self, text='Y Pos:')
        self.ypos_entry = tk.Entry(self)
        self.ypos_label.grid(row=2, column=1)
        self.ypos_entry.grid(row=3, column=1)

        self.xscale_label = tk.Label(self, text='X Scale %:')
        self.xscale_entry = tk.Entry(self)
        self.xscale_label.grid(row=2, column=2)
        self.xscale_entry.grid(row=3, column=2)
        self.yscale_label = tk.Label(self, text='Y Scale %:')
        self.yscale_entry = tk.Entry(self)
        self.yscale_label.grid(row=2, column=3)
        self.yscale_entry.grid(row=3, column=3)

        self.rotation_scale = tk.Scale(self, from_=0, to=360, resolution=1, orient=tk.HORIZONTAL, label='Rotation')
        self.rotation_scale.set(0)
        self.rotation_scale.grid(row=4, column=0, columnspan=2)
        self.trans_scale = tk.Scale(self, from_=0, to=256, resolution=1, orient=tk.HORIZONTAL, label='Opacity')
        self.trans_scale.set(256)
        self.trans_scale.grid(row=4, column=2, columnspan=2)

        self.xcrop_label = tk.Label(self, text='Left Crop(%):')
        self.xcrop_entry = tk.Entry(self)
        self.xcrop_label.grid(row=5, column=0)
        self.xcrop_entry.grid(row=6, column=0)
        self.ycrop_label = tk.Label(self, text='Top Crop(%):')
        self.ycrop_entry = tk.Entry(self)
        self.ycrop_label.grid(row=5, column=1)
        self.ycrop_entry.grid(row=6, column=1)

        self.wcrop_label = tk.Label(self, text='Right Width(%):')
        self.wcrop_entry = tk.Entry(self)
        self.wcrop_label.grid(row=5, column=2)
        self.wcrop_entry.grid(row=6, column=2)
        self.hcrop_label = tk.Label(self, text='Bottom Height(%):')
        self.hcrop_entry = tk.Entry(self)
        self.hcrop_label.grid(row=5, column=3)
        self.hcrop_entry.grid(row=6, column=3)

        self.grid(row=1, column=0, columnspan=2)

    def clone(self):
        print('clone')

    def apply(self):
        print('update')

    def moveup(self):
        print('move up')

    def movedown(self):
        print('move down')

