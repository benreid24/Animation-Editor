from view.animation_editor import AnimationEditor
from controller import images as images_controller


def main():
    app = AnimationEditor()

    images_controller.init(app)

    app.mainloop()


if __name__ == '__main__':
    main()
