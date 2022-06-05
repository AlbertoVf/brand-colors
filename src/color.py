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
                f"{self.dest}/{self.name}_{color_hex}.png", "PNG")

    def add_external_file(self, extension):
        content = ""
        with open(f"src/{self.root}.{self.extension}", "r") as f:
            content = str(f.read())
        return content

    def create_file(self):

        name = self.name
        colors = self.colors
        html = ('<!DOCTYPE html><html lang="en">' +
                f'<head><title>{name}</title><style>{add_external_file(extension="css")}</style></head>' +
                '<body><article id="colores"></article>' +
                f'<script> var colores = {colors};{add_external_file(extension="js")}</script></body></html>')

        os.system(f"mkdir -p {self.root}")
        with open(f"{self.dest}/{name}.html", "w") as file:
            file.write(html)
