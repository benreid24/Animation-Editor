# id is only unique per frame
next_id = 1

piece_template = {
    'id': next_id,
    'image_id': None,
    'img': None,

    'x': 300,
    'y': 280,
    'rotation': 0,
    'alpha': 256,

    'x_scale': 1,
    'y_scale': 1,

    'left_crop': 0,
    'right_crop': 0,
    'top_crop': 0,
    'bottom_crop': 0
}

# frame_id -> list[pieces]. Piece order determines rendering order
pieces = {}


def add_from_image(image_id, img, frame_id):
    global pieces
    global next_id

    piece = dict(piece_template)
    piece['id'] = next_id
    piece['img'] = img
    piece['image_id'] = image_id

    next_id += 1
    if frame_id not in pieces.keys():
        pieces[frame_id] = []
    pieces[frame_id].append(piece)

    return next_id-1


def add_from_piece(frame_id, piece):
    global next_id
    global pieces

    piece['id'] = next_id
    next_id += 1
    if frame_id not in pieces:
        pieces[frame_id] = []
    pieces[frame_id].append(piece)

    return next_id-1


def get_piece(frame_id, piece_id):
    global pieces

    if frame_id in pieces.keys():
        for piece in pieces[frame_id]:
            if piece['id'] == piece_id:
                return piece
    return None


def update_piece(frame_id, piece):
    global pieces

    if frame_id in pieces.keys():
        for i in range(0, len(pieces[frame_id])):
            if pieces[frame_id][i]['id'] == piece['id']:
                pieces[frame_id][i] = piece


def remove_piece(frame_id, piece_id):
    global pieces
    if frame_id in pieces.keys():
        pieces[frame_id] = [p for p in pieces[frame_id] if p['id'] != piece_id]
