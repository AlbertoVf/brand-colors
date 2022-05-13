class Color:
    def __init__(self, line: str):
        self.name = line.split(':')[0]
        self.colors = line.split(':')[1].split(' ')

    def __init__(self, name: str, colors: list):
        self.name = name
        self.colors = colors

    def __str__(self):
        return f"{self.name}: {self.colors}"
