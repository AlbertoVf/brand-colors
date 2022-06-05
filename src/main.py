import requests
import re
from color import Color


def read_file():
    url = 'http://brandcolors.net/download/?f=scss'
    response = requests.get(url)
    return response.text.split('\n')


def create_dict():
    file = read_file()
    colors = {}

    ex_name = re.compile(r'\$.*-?\d{0,2}:')
    ex_color = re.compile(r"#.{3,6}")
    ex_index = re.compile(r'-\d{0,2}$')

    for line in file:
        name = re.sub(ex_index, '', ex_name.findall(line)[0][1:-1])
        color = ex_color.findall(line)[0]
        if name not in colors:
            colors[name] = color
        else:
            colors[name] = f"{colors[name]} {color}"
    return colors


def main():
    colors = create_dict()
    for key, value in colors.items():
        c = Color(key[3:], value.split(' '))
        c.create_file()
        c.create_png()


if __name__ == '__main__':
    main()
