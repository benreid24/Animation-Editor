current_action = None
actions = []

action_template = {
    'type': 'action_name',
    'data': {
        'old_state': 'Just an example',
        'new_state': 'Not all actions would be like this'
    }
}

VALID_TYPES = [
    'save',

    'add_piece',
    'delete_piece',
    'update_piece',
    'move_piece',

    'add_image',
    'delete_image',

    'add_frame',
    'move_frame',
    'delete_frame',
    'update_frame'
]