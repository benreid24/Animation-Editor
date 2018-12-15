from controller import actions as controller
from model import actions as model
from model import images as images_model
from model import frames as frames_model
from model import pieces as pieces_model
from controller import pieces as pieces_controller
from controller import frames as frames_controller
from controller import images as images_controller
from view import util as view_util


def undo():
    if model.current_action is not None and model.current_action in range(1, len(model.actions)):
        action = model.actions[model.current_action]
        data = action['data']

        if action['type'] == 'add_piece':
            pieces_model.remove_piece(data['frame_id'], data['piece']['id'])
            pieces_controller.update_view()

        elif action['type'] == 'update_piece':
            pieces_model.update_piece(data['frame_id'], data['old'])
            pieces_controller.update_view()

        elif action['type'] == 'delete_piece':
            pieces_model.add_from_piece(data['frame_id'], data['piece'])
            pieces_controller.update_view()

        elif action['type'] == 'move_piece':
            i = 0
            for p in pieces_model.pieces[data['frame_id']]:
                if p['id'] == data['piece_id']:
                    break
                i += 1
            ni = i - data['index_change']
            temp = pieces_model.pieces[data['frame_id']][i]
            pieces_model.pieces[data['frame_id']][i] = pieces_model.pieces[data['frame_id']][ni]
            pieces_model.pieces[data['frame_id']][ni] = temp
            pieces_controller.update_view()

        elif action['type'] == 'add_image':
            images_model.remove_image(data['id'])
            images_controller.update_view()

        elif action['type'] == 'delete_image':
            view_util.error('This cannot be undone')

        elif action['type'] == 'add_frame':
            if data['frame']['id'] in pieces_model.pieces.keys():
                del pieces_model.pieces[data['frame']['id']]
            del frames_model.frames[data['index']]
            frames_controller.update_view()
            pieces_controller.update_view()

        elif action['type'] == 'update_frame':
            i = frames_model.get_frame_position(data['frame_id'])
            frames_model.frames[i]['length'] = data['old_len']
            frames_controller.update_view()

        elif action['type'] == 'move_frame':
            i = frames_model.get_frame_position(data['frame_id'])
            ni = i - data['index_change']
            temp = frames_model.frames[i]
            frames_model.frames[i] = frames_model.frames[ni]
            frames_model.frames[ni] = temp
            frames_controller.update_view()
            pieces_controller.update_view()

        elif action['type'] == 'delete_frame':
            frames_model.frames.insert(data['index'], data['frame'])
            pieces_model.pieces[data['frame']['id']] = data['pieces']
            frames_controller.update_view()
            pieces_controller.update_view()

        elif action['type'] == 'save':
            view_util.popup('Oh Fuck', 'Your Peoplemon game save has been deleted')

        model.current_action -= 1
        controller.update_view()


def redo():
    if model.current_action is not None and model.current_action in range(0, len(model.actions)-1):
        model.current_action += 1
        controller.update_view()
