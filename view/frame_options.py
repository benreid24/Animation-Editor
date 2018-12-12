import tkinter as tk


class FrameOptions(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Frame Options', padx=3, pady=3)

        self.ins_button = tk.Button(self, text='New (insert)', command=self.create)
        self.app_button = tk.Button(self, text='New (append)', command=self.create)
        self.clone_button = tk.Button(self, text='Clone Current', command=self.clone)
        self.delete_button = tk.Button(self, text='Delete Current', command=self.delete)
        self.ins_button.grid(row=0, column=0, pady=4, padx=3)
        self.app_button.grid(row=0, column=1)
        self.clone_button.grid(row=0, column=2)
        self.delete_button.grid(row=0, column=3)

        self.len_label = tk.Label(self, text='Length(ms):')
        self.len_entry = tk.Entry(self)
        self.len_update = tk.Button(self, text='Update', command=self.update_len, background='#ff5555')
        self.len_label.grid(row=1, column=1)
        self.len_entry.grid(row=1, column=2)
        self.len_update.grid(row=1, column=3)

        self.frame_list_frame = tk.LabelFrame(self, text='Frames')
        self.scrollbar = tk.Scrollbar(self.frame_list_frame)
        self.frame_list = tk.Listbox(self.frame_list_frame, yscrollcommand=self.scrollbar.set)
        for i in range(1000):
            self.frame_list.insert(tk.END, str(i))
        self.frame_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.frame_list.yview)
        self.frame_list_frame.grid(column=4, row=0, rowspan=2, padx=3)

        self.grid(row=0, column=0, padx=3, pady=20)

    def create(self):
        print('create')

    def clone(self):
        print('clone')

    def delete(self):
        print('delete')

    def update_len(self):
        print('len updated to '+self.len_entry.get())
