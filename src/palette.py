import json
import os

import requests
from PIL import Image


class Palette:
    """
    Create a pallete color with name, file result and colors
    """
    root = "brand-colors"

    def __init__(self, name: str, colors: list):
        self.name = name
        self.colors = colors
        self.dest = f"{self.root}/{self.name}"

    def __str__(self) -> str:
        return f"{self.name}: {self.colors}"

    @staticmethod
    def get_data() -> list[str]:
        """
        It downloads a file from the internet, saves it, and returns the contents of the file
        as a list of strings
        :return: A list of strings.

        """
        os.system(f"mkdir -p {Palette.root}")
        response = requests.get(
            'http://brandcolors.net/download/?f=scss', timeout=10)
        text = response.text
        with open(f"{Palette.root}/brand-colors.scss", "w", encoding="utf-8") as file:
            file.write(text)
        return text.split('\n')

    def create_png(self):
        """
        It takes a hex color code, converts it to RGB, creates a 200x200 image with that color,
        and saves it to a file
        """
        for color_hex in self.colors:
            if len(color_hex) != 7:
                color_hex = f"#{color_hex[1] * 2}{color_hex[2] * 2}{color_hex[3] * 2}"

            color = (
                int(color_hex[1:3], 16),
                int(color_hex[3:5], 16),
                int(color_hex[5:7], 16)
            )

            img = Image.new("RGB", (200, 200), color)
            img.save(f"{self.dest}/{color_hex}.png", "PNG")

    def create_file(self):
        """
        It reads the template file, replaces the placeholders with the values of the object's
        attributes, and writes the result to a new file
        """
        os.system(f"mkdir -p {self.dest}")
        with open('src/color_template.html', 'r', encoding="utf-8") as file:
            content = file.read()
            content = content.replace('{ name }', self.name)
            content = content.replace('{ colors }', str(self.colors))
        with open(f"{self.dest}/{self.name}.html", "w", encoding="utf-8") as file:
            file.write(content)

    def save_as_json(self):
        """
        We create a dictionary with the name of the color as the key and the hex value as the value.

        We then write the dictionary to a json file.

        The json file is saved in the same directory as the script.

        The name of the json file is the same as the name of the image.

        The json file is indented and sorted.
        """
        my_dict = {
            f"{self.name}-{i + 1}": self.colors[i] for i in range(len(self.colors))}
        with open(f"{self.dest}/{self.name}.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(my_dict, indent=2, sort_keys=True))
