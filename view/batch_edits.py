import tkinter as tk


class BatchEdits(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Batch Edit')

        self.appply_but = tk.Button(self, text='Apply', command=self.apply, background='#ff5555')
        self.appply_but.grid(row=0, column=2, padx=3)

        self.change_type = tk.IntVar()
        self.type_box = tk.Checkbutton(self, text='Percent Change', var=self.change_type)
        self.type_box.grid(row=0, column=3, rowspan=1, pady=10)

        self.fframe_label = tk.Label(self, text='First Frame:')
        self.fframe_entry = tk.Entry(self)
        self.fframe_label.grid(row=1, column=0)
        self.fframe_entry.grid(row=1, column=1)
        self.lframe_label = tk.Label(self, text='Last Frame:')
        self.lframe_entry = tk.Entry(self)
        self.lframe_label.grid(row=1, column=2)
        self.lframe_entry.grid(row=1, column=3)

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

        self.xcrop_label = tk.Label(self, text='X Crop(%):')
        self.xcrop_entry = tk.Entry(self)
        self.xcrop_label.grid(row=5, column=0)
        self.xcrop_entry.grid(row=6, column=0)
        self.ycrop_label = tk.Label(self, text='Y Crop(%):')
        self.ycrop_entry = tk.Entry(self)
        self.ycrop_label.grid(row=5, column=1)
        self.ycrop_entry.grid(row=6, column=1)

        self.wcrop_label = tk.Label(self, text='Crop Width(%):')
        self.wcrop_entry = tk.Entry(self)
        self.wcrop_label.grid(row=5, column=2)
        self.wcrop_entry.grid(row=6, column=2)
        self.hcrop_label = tk.Label(self, text='Crop Height(%):')
        self.hcrop_entry = tk.Entry(self)
        self.hcrop_label.grid(row=5, column=3)
        self.hcrop_entry.grid(row=6, column=3)

        self.grid(row=2, column=0, columnspan=2, pady=20)

    def apply(self):
        print('apply')
