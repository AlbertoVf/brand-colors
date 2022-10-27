import json
import os

import requests
from PIL import Image


class Palette:
    root = "brand-colors"

    def __init__(self, name: str, colors: list):
        self.name = name
        self.colors = colors
        self.dest = f"{self.root}/{self.name}"

    def __str__(self) -> str:
        return f"{self.name}: {self.colors}"

    @staticmethod
    def get_data() -> [str]:
        os.system(f"mkdir -p {Palette.root}")
        response = requests.get('http://brandcolors.net/download/?f=scss')
        text = response.text
        with open(f"{Palette.root}/brand-colors.scss", "w") as file:
            file.write(text)
        return text.split('\n')

    def create_png(self):
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
        os.system(f"mkdir -p {self.dest}")
        with open('src/color_template.html', 'r') as f:
            content = f.read()
            content = content.replace('{ name }', self.name)
            content = content.replace('{ colors }', str(self.colors))
        with open(f"{self.dest}/{self.name}.html", "w") as file:
            file.write(content)

    def save_as_json(self):
        myDict = {f"{self.name}-{i + 1}": self.colors[i] for i in range(len(self.colors))}
        with open(f"{self.dest}/{self.name}.json", "w") as file:
            file.write(json.dumps(myDict, indent=2, sort_keys=True))