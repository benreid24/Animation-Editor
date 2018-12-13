
_active_frame = 1
next_id = 2
frames = [
    {
        'id': 1,
        'length': 100
    }
]

frame_template = {
    'id': next_id,
    'length': 50
}


def init():
    global next_id
    global frames
    global _active_frame

    next_id = 2
    frames = [
        {
            'id': 1,
            'length': 50
        }
    ]
    _active_frame = 1


def active_frame():
    return _active_frame


def get_new_frame():
    global next_id

    frame = {
        'id': next_id,
        'length': 50
    }
    next_id += 1
    return frame


def get_frame(frame_id):
    for frame in frames:
        if frame['id'] == frame_id:
            return frame
    return None


def get_frame_from_pos(i):
    if i in range(0, len(frames)):
        return frames[i]
    return None


def get_frame_position(frame_id):
    for i in range(0, len(frames)):
        if frames[i]['id'] == frame_id:
            return i
    return None

