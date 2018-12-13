import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image

from controller import pieces as pieces_controller
from model import images as model
from view import util

main_view = None
image_list_view = None


def init(anim_editor):
    global main_view
    global image_list_view

    main_view = anim_editor
    image_list_view = main_view.get_image_list()


def import_image():
    global main_view
    global image_list_view

    filename = askopenfilename(
        filetypes=[
            ('Images', '*.jpg *.png')
        ]
    )
    if filename:
        try:
            img = Image.open(filename)
        except:
            util.error('Failed to open image: ' + filename)
            return
        image_id = model.add_image(img, filename)
        image_list_view.add_image(image_id, img)


def delete_image():
    image_id = image_list_view.get_selected_image()
    pieces = pieces_controller.get_pieces_using_image(image_id)
    if len(pieces) > 0:
        r = util.yesnobox('This image is used in the animation. Removing it will remove it from all frames. Delete it?')
        if r == tk.YES:
            for pid in pieces:
                pieces_controller.remove_piece(pid)
        else:
            return
    image_list_view.remove_image(image_id)
    model.remove_image(image_id)


def clone_horizontal():
    image_id = image_list_view.get_selected_image()
    img = model.get_image(image_id)
    if img is not None:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        file = 'image_{}_flipped_h.png'.format(image_id)
        new_id = model.add_image(img, file)
        image_list_view.add_image(new_id, img)


def clone_vertical():
    image_id = image_list_view.get_selected_image()
    img = model.get_image(image_id)
    if img is not None:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        file = 'image_{}_flipped_v.png'.format(image_id)
        new_id = model.add_image(img, file)
        image_list_view.add_image(new_id, img)
