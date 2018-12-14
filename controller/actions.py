from model import actions as model


def add_action(action):
    if model.current_action is not None and model.current_action < len(model.actions)-1:
        model.actions = model.actions[:model.current_action+1]
    model.actions.append(action)
    model.current_action = len(model.actions)-1


def dirty_state():
    if model.current_action is not None:
        return model.actions[model.current_action]['type'] != 'save'
    return False


def reset():
    model.actions = []
    model.current_action = None


def add_image_action(image_id):
    action = {
        'type': 'add_image',
        'data': {
            'id': image_id  # Don't bother with file, cannot redo add
        }
    }
    add_action(action)


def delete_image_action():
    action = {
        'type': 'delete_image'
    }
    add_action(action)


def add_piece_action(frame_id, piece):
    action = {
        'type': 'add_piece',
        'data': {
            'piece': piece,
            'frame_id': frame_id
        }
    }
    add_action(action)


def update_piece_action(frame_id, old_piece, new_piece):
    action = {
        'type': 'update_piece',
        'data': {
            'old': old_piece,
            'new': new_piece,
            'frame_id': frame_id
        }
    }
    add_action(action)


def move_piece_action(frame_id, piece_id, index_change):
    action = {
        'type': 'move_piece',
        'data': {
            'frame_id': frame_id,
            'piece_id': piece_id,
            'index_change': index_change
        }
    }
    add_action(action)


def delete_piece_action(frame_id, piece):
    action = {
        'type': 'delete_piece',
        'data': {
            'piece': piece,
            'frame_id': frame_id
        }
    }
    add_action(action)


def add_frame_action(frame, index, pieces):
    action = {
        'type': 'add_frame',
        'data': {
            'frame': frame,
            'index': index,
            'pieces': pieces
        }
    }
    add_action(action)


def move_frame_action(frame_id, index_change):
    action = {
        'type': 'move_frame',
        'data': {
            'frame_id': frame_id,
            'index_change': index_change
        }
    }
    add_action(action)


def update_frame_action(frame_id, old_len, new_len):
    action = {
        'type': 'update_frame',
        'data': {
            'frame_id': frame_id,
            'old_len': old_len,
            'new_len': new_len
        }
    }
    add_action(action)


def delete_frame_action(frame, index, pieces):
    action = {
        'type': 'delete_frame',
        'data': {
            'frame_id': frame,
            'index': index,
            'pieces': pieces
        }
    }
    add_action(action)


def save_action():
    action = {
        'type': 'save'
    }
    add_action(action)
