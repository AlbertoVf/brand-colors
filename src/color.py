from PIL import Image
import os


class Color:
    root = "brand-colors"

    def __init__(self, line: str):
        self.name = line.split(':')[0]
        self.colors = line.split(':')[1].split(' ')
        self.dest = f"{self.root}/{self.name}"

    def __init__(self, name: str, colors: list):
        self.name = name
        self.colors = colors
        self.dest = f"{self.root}/{self.name}"

    def __str__(self):
        return f"{self.name}: {self.colors}"

    def create_png(self):
        for color_hex in self.colors:
            if len(color_hex) != 7:
                color_hex = f"#{color_hex[1]*2}{color_hex[2]*2}{color_hex[3]*2}"

            color = (
                int(color_hex[1:3], 16),
                int(color_hex[3:5], 16),
                int(color_hex[5:7], 16)
            )

            img = Image.new("RGB", (200, 200), color)
            img.save(
                f"{self.dest}/{color_hex}.png", "PNG")

    def create_file(self):
        os.system(f"mkdir -p {self.dest}")
        with open('src/color_template.html', 'r') as f:
            content = f.read()
            content = content.replace('{ name }', self.name)
            content = content.replace('{ colors }', str(self.colors))
        with open(f"{self.dest}/{self.name}.html", "w") as file:
            file.write(content)
