import tkinter as tk


class FrameOptions(tk.LabelFrame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Frame Options', padx=3, pady=3)

        self.new_button = tk.Button(self, text='New', command=self.create)
        self.clone_button = tk.Button(self, text='Clone Current', command=self.clone)
        self.delete_button = tk.Button(self, text='Delete Current', command=self.delete)
        self.new_button.grid(row=0, column=0, pady=4)
        self.clone_button.grid(row=0, column=1)
        self.delete_button.grid(row=0, column=2)

        self.len_label = tk.Label(self, text='Length(ms):')
        self.len_entry = tk.Entry(self)
        self.len_update = tk.Button(self, text='Update', command=self.update_len)
        self.len_label.grid(row=1, column=0)
        self.len_entry.grid(row=1, column=1)
        self.len_update.grid(row=1, column=2)

        self.grid(row=0, column=0)

    def create(self):
        print('create')

    def clone(self):
        print('clone')

    def delete(self):
        print('delete')

    def update_len(self):
        print('len updated to '+self.len_entry.get())
