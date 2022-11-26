import re

from src.palette import Palette


def create_dict(file: list[str] = Palette.get_data()) -> dict:
    """
    It takes a list of strings, and returns a dictionary of colors

    :param file: list[str] = Palette.get_data()
    :type file: list[str]
    :return: A dictionary with the color names as keys and the color values as values.
    """

    colors = {}

    ex_name = re.compile(r'\$.*-?\d{0,2}:')
    ex_color = re.compile(r"#[\da-fA-F]{3,6}")
    ex_index = re.compile(r'-\d{0,2}$')

    for line in file:
        name = re.sub(ex_index, '', ex_name.findall(line)[0][1:-1])[3:]
        color = ex_color.findall(line)[0]
        if name not in colors:
            colors[name] = color
        else:
            if color not in colors[name]:
                colors[name] = f"{colors[name]} {color}"
    return colors


def main():
    """
    `main()` creates a dictionary of colors, creates a `Palette` object for each color,
    creates a file for each color, creates a png for each color,
    and saves each color as a json file.
    """
    colors = create_dict()
    for key, value in colors.items():
        color = Palette(key, value.split(' '))
        color.create_file()
        color.create_png()
        color.save_as_json()


if __name__ == '__main__':
    main()
