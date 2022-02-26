
class Animal:

    def __init__(self, name):
        self.color = None
        self.name = name

    def set_animal_color(self, color):
        self.color = color

    def get_animal_color(self):
        return self.color
