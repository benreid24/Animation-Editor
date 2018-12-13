import tkinter.messagebox as mbox
import tkinter as tk


def popup(title, message):
    mbox.showinfo(title, message)


def error(message):
    mbox.showerror('Error', message)


def yesnobox(question):
    return mbox.askyesno('WTF', question) == tk.YES
