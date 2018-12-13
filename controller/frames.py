from model import frames as model
from model import pieces as pieces_model


def new_frame_append():
    model.frames.append(model.get_new_frame())


def new_frame_insert():
    i = model.get_frame_position(model.active_frame())
    model.frames.insert(i, model.get_new_frame())


def clone_frame():
    i = model.get_frame_position(model.active_frame())
    frame = dict(model.get_frame_from_pos(i))
    model.frames.insert(i+1, frame)
    pieces_model[frame['id']] = dict(pieces_model[model.active_frame()])


def delete_frame():
    frame = model.get_frame(model.active_frame())
    model.frames.remove(frame)
    del pieces_model.pieces[frame['id']]


def move_frame_up():
    i = model.get_frame_position(model.active_frame())
    ni = i -1
    if ni >= 0:
        temp = model.frames[ni]
        model.frames[ni] = model.frames[i]
        model.frames[i] = temp


def move_frame_down():
    i = model.get_frame_position(model.active_frame())
    ni = i + 1
    if ni < len(model.frames):
        temp = model.frames[ni]
        model.frames[ni] = model.frames[i]
        model.frames[i] = temp


def change_active_frame():
    # TODO Get new frame pos from view and update active frame
    # TODO Update view with new pieces/etc
    print('new active frame')


def update_frame():
    new_len = 50
    # TODO Get length from view
    i = model.get_frame_position(model.active_frame())
    model.frames[i]['length'] = new_len
