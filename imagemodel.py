from kivy.uix.image import Image
from kivy.properties import NumericProperty


class ImageModel(Image):

    ang = NumericProperty()

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)

    def rotate_right(self):
        self.ang += 90

    def rotate_left(self):
        self.ang -= 90

    def reset_angle(self):
        self.ang = 0
