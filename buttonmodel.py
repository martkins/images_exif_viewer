import exifread
from kivy.uix.button import Button
from kivy.lang import Builder
from tkinter.filedialog import askopenfilenames
from kivy.properties import DictProperty, ListProperty, NumericProperty
import webbrowser
from tkinter import Tk
root = Tk()
root.withdraw()

Builder.load_file('./actionbutton.kv')


def _convert(value):
    d = float(str(value[0]))
    m = float(str(value[1]))
    s1 = (str(value[2])).split('/')
    s = float((s1[0])) / float((s1[1]))
    return d + (m / 60.0) + (s / 3600.0)


class ButtonModel(Button):

    tags = DictProperty()
    images = ListProperty()
    count = NumericProperty(0)

    def __init__(self,image='', labels='', **kwargs):
        self.image = image
        self.labels = labels
        super(Button, self).__init__(**kwargs)

    def rotate_right(self):
        self.image.model.rotate_right()

    def rotate_left(self):
        self.image.model.rotate_left()

    def open_image(self):
        try:
            self.images = askopenfilenames(initialdir="/", title="Select file",
                                  filetypes=(("jpeg files", "*.jpg"),("png files","*png"), ("all files", "*.*")))
            self.reset_labels()
            self.image.source = self.images[0]
            self.image.model.reset_angle()
        except:
            pass

    def get_exif_data(self):
        print(self.image.source)
        f = open(self.image.source, 'rb')
        self.tags = exifread.process_file(f)
        i = 0
        for tag in self.tags.keys():
            if tag not in ('EXIF MakerNote','User Comment','JPEGThumbnail', 'EXIF UserComment'):
                self.labels[i].text = str(tag.split()[1])+' : '+str(self.tags[tag])
                i = i+1

    def get_location(self):
        lat = None
        lon = None

        try:
            gps_latitude = self.tags['GPS GPSLatitude'].values
            gps_latitude_ref = self.tags['GPS GPSLatitudeRef'].values
            gps_longitude = self.tags['GPS GPSLongitude'].values
            gps_longitude_ref = self.tags['GPS GPSLongitudeRef'].values

            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = _convert(gps_latitude)
                if gps_latitude_ref != 'N':
                    lat = 0 - lat

                lon = _convert(gps_longitude)
                if gps_longitude_ref != 'E':
                    lon = 0 - lon

            webbrowser.open('https://www.google.com/maps/search/?api=1&query='+str(lat)+','+str(lon))
        except:
            pass

    def next_image(self):
        if len(self.images) > 1:
            self.count = self.count + 1
            if self.count >= len(self.images):
                self.count = 0
            self.image.model.reset_angle()
            self.reset_labels()
            self.image.source = self.images[self.count]

    def previous_image(self):
        if len(self.images) > 1:
            self.count = self.count - 1
            if self.count < 0:
                self.count = len(self.images)-1
            self.image.model.reset_angle()
            self.reset_labels()
            self.image.source = self.images[self.count]

    def reset_labels(self):
        self.tags.clear()
        for i in range(0,len(self.labels)):
            self.labels[i].text = ''