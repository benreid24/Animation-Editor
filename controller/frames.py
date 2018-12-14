from model import frames as model
from model import pieces as pieces_model
from controller import pieces as pieces_controller
from view import util

view_options = None


def init(main_view):
    global view_options

    view_options = main_view.get_frame_controls()
    view_options.set_length(model.frames[0]['length'])
    model.init()


def _update_view():
    i = model.get_frame_position(model.active_frame())
    length = model.get_frame_from_pos(i)['length']
    view_options.set_frame_count(len(model.frames))
    view_options.set_active(i)
    view_options.set_length(length)


def new_frame_append():
    model.frames.append(model.get_new_frame())
    _update_view()


def new_frame_insert():
    i = model.get_frame_position(model.active_frame())
    model.frames.insert(i, model.get_new_frame())
    _update_view()


def clone_frame():
    i = model.get_frame_position(model.active_frame())
    frame = dict(model.get_frame(model.active_frame()))
    frame['id'] = model.next_id
    model.next_id += 1
    model.frames.insert(i+1, frame)
    if model.active_frame() in pieces_model.pieces.keys():
        pieces_model.pieces[frame['id']] = [dict(p) for p in pieces_model.pieces[model.active_frame()]]
    _update_view()


def delete_frame():
    if len(model.frames) > 1:
        i = model.get_frame_position(model.active_frame())
        frame = model.get_frame(model.active_frame())

        ni = i + 1
        if ni >= len(model.frames):
            ni = len(model.frames) - 2  # Deleting last, next is second last
        model._active_frame = model.get_frame_from_pos(ni)['id']

        pieces_controller.change_active_frame(frame['id'], model.active_frame())
        model.frames.remove(frame)
        if frame['id'] in pieces_model.pieces.keys():
            del pieces_model.pieces[frame['id']]

        _update_view()

    else:
        util.error('You need to have at least one frame, jackass')


def move_frame_up():
    i = model.get_frame_position(model.active_frame())
    ni = i - 1
    if ni >= 0:
        temp = model.frames[ni]
        model.frames[ni] = model.frames[i]
        model.frames[i] = temp
        _update_view()


def move_frame_down():
    i = model.get_frame_position(model.active_frame())
    ni = i + 1
    if ni < len(model.frames):
        temp = model.frames[ni]
        model.frames[ni] = model.frames[i]
        model.frames[i] = temp
        _update_view()


def change_active_frame():
    old = model.active_frame()
    model._active_frame = model.get_frame_from_pos(view_options.get_selected_index())['id']
    pieces_controller.change_active_frame(old, model.active_frame())
    _update_view()


def update_frame():
    new_len = view_options.get_length_str()
    try:
        new_len = int(new_len)
    except:
        util.error('Frame length must be an integer')
        return
    if new_len <= 0:
        util.error('Frame length <= 0 ?!')
        return
    i = model.get_frame_position(model.active_frame())
    model.frames[i]['length'] = new_len
