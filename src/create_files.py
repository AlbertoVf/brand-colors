import os
from color import Color


def style_css():
    return "canvas { width: 200px; height: 200px; margin: 2%; border: 2px solid #000; padding: 5px;}article { margin: 5% auto; width: 90%;}"


def script_js():
    return(
        'for (var i=0;i < colores.length;i++) {' +
        'var div=document.createElement("canvas");document.getElementById("colores").appendChild(div);' +
        'var id="canvas-"+[i+1];div.setAttribute("id", id);var canvas=document.getElementById(id);' +
        'var ctx=canvas.getContext("2d");ctx.fillStyle=colores[i];ctx.fillRect(0, 0, canvas.width, canvas.height);' +
        'console.log("Canvas: " + (i+1) + " -  color: " + colores[i])}'
    )


def set_html(color: Color):
    name = color.name
    colors = color.colors
    html = ('<!DOCTYPE html><html lang="en">' +
            f'<head><title>{name}</title><style>{style_css()}</style></head>' +
            '<body><article id="colores"></article>' +
            f'<script> var colores = {colors};{script_js()}</script></body></html>')
    return html


def create_file(color: Color):
    name = color.name
    html = set_html(color)
    dest = f"brand-colors/{name}"

    os.system(f"mkdir -p {dest}")
    with open(f"{dest}/{name}.html", "w") as file:
        file.write(html)
