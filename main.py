import re

from src.palette import Palette


def create_dict(file: [str] = Palette.get_data()) -> dict:
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
    colors = create_dict()
    for key, value in colors.items():
        c = Palette(key, value.split(' '))
        c.create_file()
        c.create_png()
        c.save_as_json()

if __name__ == '__main__':
    main()
