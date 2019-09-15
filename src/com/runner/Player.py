import random

from colorama import Fore, Style

color_dictionary = (Fore.MAGENTA, Fore.BLUE)
used_colors = []


class Player:

    def __init__(self, name, move_style, color):
        self.name = name
        self.move_style = move_style
        self.color = color

    @classmethod
    def player_from_input(cls, name, move_style):
        rand_item = random.choice(color_dictionary)
        while rand_item in used_colors:
            rand_item = random.choice(color_dictionary)

        used_colors.append(rand_item)
        return cls(name, move_style, rand_item)

    def __str__(self):
        return f'{self.color}Player details - name: {self.name}, move_style: {self.move_style}, color: {self.color} ' + Style.RESET_ALL
