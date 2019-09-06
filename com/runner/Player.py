class Player:
    name = ''
    move_style = ''
    move_color = ''
    info_color = ''

    def __init__(self, name):
        self.name = name

    def set_move_style(self, style):
        self.move_style = style

    def colorize_player(self, color):
        self.move_color = color['bold']
        self.info_color = color['normal']

    def __str__(self):
        return f'\033{self.info_color}Player details - name: {self.name}, move_style: {self.move_style} \033[0:30m'
