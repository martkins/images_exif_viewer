# ImageExifViewer

This project is a simple image viewer written in Python: this is an academic exercise from a course at Università degli Studi di Firenze.


## Requirements
| Software  | Version | 
|:--------------------------------------------------------------:|:-------:|
| [Python](https://www.python.org)                               | 3.6     |
| [Kivy](https://kivy.org/#home)                                 | 1.10.1  |
| [ExifRead](https://pypi.org/project/ExifRead/)                 | 2.1.2   |

## Launch the applications
Run the python main file from the directory of project:
```
python main.py
```

## Usage
To **load** an image (or multiple) click on Open Image or CTRL+O.

To **show the EXIF tags** of the selected image, click on Get Exif Data or CTRL+E.

To **rotate**  an image, click on Rotate Right/Left (90°Clockwise or 90° counterclockwise) or CTRL+R/CTRL+L.

To open **GPS Coordinates** on Google Maps on web browser, click on Google Maps or CTRL+G: this feature is available only if in the list of exif tags there are all the coordinates required.

To navigate trought multiple images, click on Next/Previous Image or CTRL+N/CTRL+P.

