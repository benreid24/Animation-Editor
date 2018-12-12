import tkinter as tk


class InterpolateControls(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Interpolate Frames')

        self.time_label = tk.Label(self, text='Time (ms):')
        self.time_entry = tk.Entry(self)
        self.time_label.grid(row=0, column=0)
        self.time_entry.grid(row=0, column=1)

        self.maxlen_label = tk.Label(self, text='Max Frame Length (ms):')
        self.maxlen_entry = tk.Entry(self)
        self.maxlen_entry.insert(0, '10')
        self.maxlen_label.grid(row=0, column=2)
        self.maxlen_entry.grid(row=0, column=3)

        self.frame_label = tk.Label(self, text='Start Frame (interpolates to following frame):')
        self.frame_entry = tk.Entry(self)
        self.frame_label.grid(row=1, column=0, columnspan=2)
        self.frame_entry.grid(row=1, column=2)

        self.apply_but = tk.Button(self, text='Generate Frames', command=self.apply, background='#ff5555')
        self.apply_but.grid(row=1, column=3, padx=5)

        self.grid(row=3, column=0)

    def apply(self):
        print('apply')
