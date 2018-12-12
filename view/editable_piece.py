import tkinter as tk
from PIL import ImageTk, Image

_TOP = 0
_RIGHT = 1
_BOTTOM = 2
_LEFT = 3


class EditablePiece:
    def _get_scale_rect(self):
        return {
            'x': self.position[0] + self.img.width() - 10,
            'y': self.position[1] + self.img.height() - 10,
            'w': self.position[0] + self.img.width(),
            'h': self.position[1] + self.img.height()
        }

    def _get_crop_rect(self, c):
        if c % 2 != 0:
            w = 5
            h = 10
            y = self.position[1] + self.img.height()/2 - w/2
            x = self.position[0]
            if c == 1:
                x += self.img.width() - w
        else:
            w = 10
            h = 5
            x = self.position[0] + self.img.width()/2 - w/2
            y = self.position[1]
            if c == 2:
                y += self.img.height() - h
        return {
            'x': x,
            'y': y,
            'w': x+w,
            'h': y+h
        }

    def _get_crop_box(self):
        return (
            self.raw_image.size[0] * self.crops[3],
            self.raw_image.size[1] * self.crops[0],
            self.raw_image.size[0] - self.raw_image.size[0] * self.crops[1],
            self.raw_image.size[1] - self.raw_image.size[1] * self.crops[2]
        )

    def _update_items(self):
        self.canvas.delete(self.image_id)

        self.transformed_image = self.raw_image.crop(self._get_crop_box())
        self.transformed_image = self.transformed_image.resize(
            (int(self.transformed_image.size[0]*self.scale[0]),
             int(self.transformed_image.size[1]*self.scale[1]))
        )
        self.transformed_image = self.transformed_image.rotate(self.rotation, expand=True)
        # TODO transparency
        self.img = ImageTk.PhotoImage(self.transformed_image)
        self.image_id = self.canvas.create_image(
            self.position[0],
            self.position[1],
            image=self.img,
            anchor=tk.NW
        )
        self.canvas.tag_bind(self.image_id, '<Button-1>', self._start_move)
        self.canvas.tag_bind(self.image_id, '<B1-Motion>', self._move_drag)
        self.canvas.tag_bind(self.image_id, '<ButtonRelease-1>', self._stop_move)

        self.canvas.delete(self.outline_id)
        self.outline_id = self.canvas.create_rectangle(
            self.position[0],
            self.position[1],
            self.position[0]+self.img.width(),
            self.position[1]+self.img.height(),
            fill=''
        )
        self.canvas.delete(self.scale_id)
        rect = self._get_scale_rect()
        self.scale_id = self.canvas.create_rectangle(rect['x'], rect['y'], rect['w'], rect['h'], fill='black')
        self.canvas.tag_bind(self.scale_id, '<Button-1>', self._start_scale)
        self.canvas.tag_bind(self.scale_id, '<ButtonRelease-1>', self._stop_scale)

        for i in range(0, 4):
            rect = self._get_crop_rect(i)
            self.canvas.delete(self.crop_ids[i])
            self.crop_ids[i] = self.canvas.create_rectangle(rect['x'], rect['y'], rect['w'], rect['h'], fill='black')
            self.canvas.tag_bind(self.crop_ids[i], '<Button-1>', self._start_crop)
            self.canvas.tag_bind(self.crop_ids[i], '<ButtonRelease-1>', self._stop_crop)

        self.set_active(self.state['active'])

    def _move_items(self, dx, dy):
        self.canvas.move(self.image_id, dx, dy)
        self.canvas.move(self.outline_id, dx, dy)
        self.canvas.move(self.scale_id, dx, dy)
        for i in range(0, 4):
            self.canvas.move(self.crop_ids[i], dx, dy)

    def _hide_items(self):
        self.canvas.itemconfig(self.outline_id, state=tk.HIDDEN)
        self.canvas.itemconfig(self.scale_id, state=tk.HIDDEN)
        for i in range(0, 4):
            self.canvas.itemconfig(self.crop_ids[i], state=tk.HIDDEN)

    def _show_items(self):
        self.canvas.itemconfig(self.outline_id, state=tk.NORMAL)
        self.canvas.itemconfig(self.scale_id, state=tk.NORMAL)
        for i in range(0, 4):
            self.canvas.itemconfig(self.crop_ids[i], state=tk.NORMAL)

    def _start_move(self, event):
        self.set_active(True)
        self.state['moving'] = True
        self.state['orig_pos'] = self.position
        self.state['click_pos'] = (event.x, event.y)

    def _move_drag(self, event):
        if self.state['moving'] and self.state['active']:
            dx = event.x - self.state['click_pos'][0]
            dy = event.y - self.state['click_pos'][1]
            self._move_items(dx, dy)
            self.position = (self.position[0]+dx, self.position[1]+dy)
            self.state['click_pos'] = (event.x, event.y)

    def _stop_move(self, event):
        if self.state['moving'] and self.state['active']:
            self.state['moving'] = False
            # TODO move model

    def _start_scale(self, event):
        if self.state['active']:
            self.state['moving'] = False
        self.state['orig_scale'] = self.scale
        self.state['scaling'] = True

    def _stop_scale(self, event):
        if self.state['scaling'] and self.state['active']:
            self.state['scaling'] = False
            nw = event.x - self.position[0]
            nh = event.y - self.position[1]
            sx = nw / self.raw_image.size[0] / (1 - self.crops[_RIGHT] - self.crops[_LEFT])
            sy = nh / self.raw_image.size[1] / (1 - self.crops[_TOP] - self.crops[_BOTTOM])
            self.scale = (sx, sy)
            self._update_items()
            # TODO scale model

    def _start_crop(self, event):
        if self.state['active']:
            self.state['moving'] = False
            self.state['cropping'] = True
            crop_ids = self.canvas.find_overlapping(event.x, event.y, event.x + 2, event.y + 2)
            for i in range(0, 4):
                if self.crop_ids[i] in crop_ids:
                    active_side = i
                    break
            self.state['orig_crop'] = self.crops
            self.state['acrop'] = active_side
            self.state['click_pos'] = (event.x, event.y)

    def _stop_crop(self, event):
        if self.state['active'] and self.state['cropping']:
            self.state['cropping'] = False

            c = self.state['acrop']
            if c % 2 == 0:
                perc_showing = 1 - self.crops[_TOP] - self.crops[_BOTTOM]
                d = self.state['click_pos'][1]-event.y
                if c == _TOP:
                    d *= -1
                perc_cut = d/self.img.height()
            else:
                perc_showing = 1 - self.crops[_RIGHT] - self.crops[_LEFT]
                d = self.state['click_pos'][0]-event.x
                if c == _LEFT:
                    d *= -1
                perc_cut = d/self.img.width()

            perc_cropped = perc_cut / perc_showing
            self.crops[c] += perc_cropped
            if self.crops[c] > 1:
                self.crops[c] = 1
            if self.crops[c] < 0:
                self.crops[c] = 0
            self._update_items()
            # TODO crop model

    def __init__(self, master, image_file, x, y):
        self.canvas = master
        self.state = {
            'active': False,
            'moving': False,
            'scaling': False,
            'cropping': False,
            'orig_pos': (x, y),
            'orig_scale': (1.0, 1.0),
            'orig_crop': [0, 0, 0, 0],
            'click_pos': (0, 0),
            'acrop': -1
        }

        self.raw_image = Image.open(image_file)
        self.transformed_image = self.raw_image.copy()
        self.img = ImageTk.PhotoImage(self.transformed_image)

        self.position = (x, y)
        self.scale = (1.0, 1.0)
        self.crops = [0, 0, 0, 0]
        self.rotation = 0

        self.image_id = 0
        self.outline_id = 0
        self.scale_id = 0
        self.crop_ids = [0, 0, 0, 0]

        self._update_items()

    def set_active(self, active):
        self.state['active'] = active
        if active:
            self._show_items()
        else:
            self._hide_items()

    def contains(self, x, y):
        return x in range(self.position[0], self.position[0]+self.img.width()) and \
               y in range(self.position[1], self.position[1]+self.img.height())
