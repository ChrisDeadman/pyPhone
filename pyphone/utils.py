import os
from enum import Enum
from tkinter.font import nametofont

from PIL import Image, ImageTk

_app_path = os.path.dirname(os.path.abspath(__file__))
_data_path = os.path.join(_app_path, "data")

_images = []


class RelativeSize(Enum):
    normal = 1
    small = 2
    big = 3


def get_user_file(relative_path):
    settings_path = os.path.expanduser("~/.pyPhone")
    if not os.path.exists(settings_path):
        os.makedirs(settings_path)
    return os.path.join(settings_path, relative_path)


def load_configuration(file_path):
    import configparser
    import shutil
    if not os.path.exists(file_path):
        shutil.copy(os.path.join(_data_path, "pyPhone.config"), file_path)
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


def load_font(relative_size):
    _default_font = nametofont("TkDefaultFont")
    size = _default_font.metrics("linespace")

    if relative_size == RelativeSize.small:
        size = int(size / 1.25)
    elif relative_size == RelativeSize.big:
        size = int(size * 1.25)

    return _default_font.name, size


def load_image(widget, image_name, relative_size=RelativeSize.normal):
    image = Image.open(os.path.join(_data_path, "images", image_name))
    image_aspect = image.width / image.height
    screen_height = widget.winfo_screenheight()
    scaling = 1

    # special scaling for very big images
    if image.height > 160:
        if screen_height < 700:
            scaling = 0.25
        elif screen_height < 1400:
            scaling = 0.5

    if relative_size == RelativeSize.normal:
        scaling /= 1.25
    elif relative_size == RelativeSize.small:
        scaling /= 16

    if scaling < 1:
        new_size = image.height * scaling
        if new_size < 16:
            new_size = 16
        image = image.resize((int(new_size * image_aspect), int(new_size)))

    photo_image = ImageTk.PhotoImage(image)
    _images.append(photo_image)
    return photo_image
