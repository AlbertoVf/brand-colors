import os
from color import Color


def add_exterlan_file(extension):
    content = ""
    with open(f"src/brand-colors.{extension}", "r") as f:
        content = str(f.read())
    return content


def set_html(color: Color):
    name = color.name
    colors = color.colors

    html = ('<!DOCTYPE html><html lang="en">' +
            f'<head><title>{name}</title><style>{add_exterlan_file("css")}</style></head>' +
            '<body><article id="colores"></article>' +
            f'<script> var colores = {colors};{add_exterlan_file("js")}</script></body></html>')

    return html


def create_file(color: Color):
    name = color.name
    html = set_html(color)
    dest = f"brand-colors/{name}"

    os.system(f"mkdir -p {dest}")
    with open(f"{dest}/{name}.html", "w") as file:
        file.write(html)
