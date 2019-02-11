from kivy.app import App
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListView, SimpleListAdapter
from kivy.uix.label import Label
from imagemodel import ImageModel
from kivy.uix.button import Button
from kivy.factory import Factory
from buttonmodel import ButtonModel
from labelmodel import LabelModel
from kivy.core.window import Window


class ButtonWithModel(Button):

    def __init__(self,model, **kwargs):
        self.model = model
        super().__init__(**kwargs)


class LabelWithModel(Label):

    def __init__(self,model, **kwargs):
        self.model = model
        super().__init__(**kwargs)


class ImageWithModel(Image):

    def __init__(self,model, **kwargs):
        self.model = model
        super().__init__(**kwargs)


class MainApp(App):

    image = ObjectProperty()
    exif = ObjectProperty()

    def build(self):
        Window.bind(on_keyboard=self.on_keyboard)
        self.start_app()

    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        if modifier == ['ctrl'] and codepoint == 'r':
            self.image.model.rotate_right()
        if modifier == ['ctrl'] and codepoint == 'l':
            self.image.model.rotate_left()
        if modifier == ['ctrl'] and codepoint == 'o':
            self.exif.model.open_image()
        if modifier == ['ctrl'] and codepoint == 'e':
            self.exif.model.get_exif_data()
        if modifier == ['ctrl'] and codepoint == 'n':
            self.exif.model.next_image()
        if modifier == ['ctrl'] and codepoint == 'p':
            self.exif.model.previous_image()
        if modifier == ['ctrl'] and codepoint == 'g':
            self.exif.model.get_location()

    def start_app(self):
        labels = [LabelModel() for _ in range(100)]

        self.image = Factory.MainImage(ImageModel())
        self.root.ids.image_box.add_widget(self.image)

        self.exif = Factory.GetExifData(ButtonModel(image=self.image, labels=labels))
        self.root.ids.button_box.add_widget(self.exif)
        right = Factory.RotateRight(self.exif.model)
        self.root.ids.button_box.add_widget(right)
        left = Factory.RotateLeft(self.exif.model)
        self.root.ids.button_box.add_widget(left)
        loc = Factory.GetLocation(self.exif.model)
        self.root.ids.button_box.add_widget(loc)
        next = Factory.NextImage(self.exif.model)
        self.root.ids.cycle_box.add_widget(next)
        prev = Factory.PreviousImage(self.exif.model)
        self.root.ids.cycle_box.add_widget(prev)
        get = Factory.OpenImage(self.exif.model)
        self.root.ids.button_box.add_widget(get)

        lab = Factory.ExifLabel(LabelModel())
        self.root.ids.exif_container.add_widget(lab)

        list_adapter = SimpleListAdapter(
            data=labels,
            args_converter=lambda row, model: {'model': model,
                                               'size_hint_y': None,
                                               'height':100},
            cls=Factory.ExifTags)
        self.root.ids.exif_container.add_widget(ListView(adapter=list_adapter))


if __name__ == "__main__":
    MainApp().run()
