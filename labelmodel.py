from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.event import EventDispatcher

class LabelModel(Label):

    def __init__(self, **kwargs):
        super(Label, self).__init__(**kwargs)



