import os

import tkinter as tk

from controller import pieces as pieces_controller
from controller import images as images_controller
from controller import frames as frames_controller
from controller import actions as actions_controller
from view import util as view_util

current_file = None


def new_anim():
    global current_file

    if actions_controller.dirty_state():
        c = view_util.yesnobox('Discard unsaved changes?')
        if c == tk.NO:
            return

    current_file = None
    images_controller.reset()
    pieces_controller.reset()
    frames_controller.reset()
    actions_controller.reset()


def open_anim():
    global current_file

    if actions_controller.dirty_state():
        c = view_util.yesnobox('Discard unsaved changes?')
        if c == tk.NO:
            return

    file = view_util.get_open_anim_file()
    if file is not None and os.path.isfile(file):
        current_file = file
        images_controller.reset()
        pieces_controller.reset()
        frames_controller.reset()
        actions_controller.reset()
        # TODO load


def save():
    global current_file

    if current_file is None:
        current_file = view_util.get_save_devanim_file()

    if current_file is not None:
        actions_controller.save_action()
        # TODO save


def save_as():
    global current_file

    current_file = view_util.get_save_devanim_file()
    if current_file is not None:
        actions_controller.save_action()
        # TODO save
