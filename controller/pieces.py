from model import pieces as model
from model import images as images_model
from model import frames as frames_model

images_view = None
pieces_view = None
canvas_view = None
active_piece = None


def init(main_view):
    global images_view
    global pieces_view
    global canvas_view
    global active_piece

    images_view = main_view.get_image_list()
    pieces_view = main_view.get_piece_controls()
    canvas_view = main_view.get_main_canvas()
    active_piece = None


def add_from_image():
    image_id = images_view.get_selected_image()
    img = images_model.get_image(image_id)
    piece_id = model.add_from_image(image_id, img, frames_model.active_frame())
    piece = model.get_piece(frames_model.active_frame(), piece_id)
    canvas_view.add_piece(piece)


def add_from_piece():
    if active_piece is not None:
        piece = model.get_piece(frames_model.active_frame(), active_piece)
        if piece is not None:
            piece = dict(piece)
            piece['x'] = 100
            piece['y'] = 100
            pid = model.add_from_piece(frames_model.active_frame(), piece)
            piece = model.get_piece(frames_model.active_frame(), pid)
            canvas_view.add_piece(piece)


def update_piece(old_piece, new_piece):
    # TODO action for undo
    fid = frames_model.active_frame()
    model.update_piece(fid, new_piece)
    canvas_view.update_piece(new_piece)
    pieces_view.update_piece(new_piece)
    _reorder_canvas()


def remove_piece():
    if active_piece is not None:
        model.remove_piece(frames_model.active_frame(), active_piece)
        canvas_view.delete_piece(active_piece)
        clear_active()


def activate_piece(piece_id):
    global active_piece

    active_piece = piece_id
    piece = model.get_piece(frames_model.active_frame(), piece_id)
    pieces_view.update_piece(piece)


def clear_active():
    global active_piece
    pieces_view.clear()
    active_piece = None


def move_piece_up():
    if active_piece is not None:
        fid = frames_model.active_frame()
        if fid in model.pieces.keys():
            index = None
            for i in range(0, len(model.pieces[fid])):
                if model.pieces[fid][i]['id'] == active_piece:
                    index = i
                    break
            if index is not None:
                ni = index + 1
                if ni < len(model.pieces[fid]):
                    temp = model.pieces[fid][index]
                    model.pieces[fid][index] = model.pieces[fid][ni]
                    model.pieces[fid][ni] = temp
                    _reorder_canvas()


def move_piece_down():
    if active_piece is not None:
        fid = frames_model.active_frame()
        if fid in model.pieces.keys():
            index = None
            for i in range(0, len(model.pieces[fid])):
                if model.pieces[fid][i]['id'] == active_piece:
                    index = i
                    break
            if index is not None:
                ni = index - 1
                if ni >= 0:
                    temp = model.pieces[fid][index]
                    model.pieces[fid][index] = model.pieces[fid][ni]
                    model.pieces[fid][ni] = temp
                    _reorder_canvas()


def _reorder_canvas():
    for p in model.pieces[frames_model.active_frame()]:
        canvas_view.update_piece(p)
