import tkinter as tk


class FrameList(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Frames')

        self.scrollbar = tk.Scrollbar(self)
        self.frame_list = tk.Listbox(self, yscrollcommand=self.scrollbar.set)
        for i in range(1000):
            self.frame_list.insert(tk.END, str(i))
        self.frame_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.frame_list.yview)

        self.grid(column=1, row=0)
