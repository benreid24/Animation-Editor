import tkinter.messagebox as mbox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk


def popup(title, message):
    mbox.showinfo(title, message)


def error(message):
    mbox.showerror('Error', message)


def yesnobox(question):
    return mbox.askyesno('WTF', question) == tk.YES


def get_image_file():
    return askopenfilename(
        title='Add Image',
        filetypes=[
            ('Images', '*.jpg *.png')
        ]
    )


def get_open_anim_file():
    return askopenfilename(
        title='Open Animation',
        filetypes=[('DevAnims', '*.danim')]
    )


def get_save_devanim_file():
    return asksaveasfilename(
        title='Save Animation',
        defaultextension='.danim',
        filetypes=[('DevAnims', '*.danim')]
    )


def get_export_file():
    return asksaveasfilename(
        title='Export Animation',
        defaultextension='.anim',
        filetypes=[('Animations', '*.anim')]
    )
