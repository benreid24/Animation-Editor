import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()


def main():
    app = Application()
    app.master.title('Sample application')
    app.mainloop()


if __name__ == '__main__':
    main()
