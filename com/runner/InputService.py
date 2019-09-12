from colorama import Fore, Style

from Player import Player


class InputService:

    def __init__(self):
        self.game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.available_tiles = list(range(1, 10))

    @staticmethod
    def get_player_names():
        player_1_name_input = input("Player 1 - Please enter you name\n")
        player_2_name_input = input("Player 2 - Please enter you name\n")
        return player_1_name_input, player_2_name_input

    @staticmethod
    def get_player_move_choice(player_1):
        input_styles = ['X', 'O']
        player_style_input = input(f"{player_1}, please pick a marker 'X' or 'O'\n")

        while player_style_input.upper() not in input_styles:
            print(Fore.RED + f'Invalid input : {player_style_input}' + Style.RESET_ALL)
            player_style_input = input(
                f"{player_1}, please choose a marker only between" + Fore.GREEN + f" {input_styles[0]} " + Style.RESET_ALL +
                "or " + Fore.GREEN + f"{input_styles[1]}" + Style.RESET_ALL)

        player1_choice = player_style_input.upper()
        input_styles.pop(input_styles.index(player_style_input.upper()))
        player2_choice = input_styles[0]

        return player1_choice, player2_choice

    def create_players(self):
        player_1_name_input, player_2_name_input = self.get_player_names()
        player_1_move, player_2_move = self.get_player_move_choice(player_1_name_input)
        player_1 = Player.player_from_input(player_1_name_input, player_1_move)
        player_2 = Player.player_from_input(player_2_name_input, player_2_move)

        return player_1, player_2

    def play_moves(self, selected_player):
        print(selected_player.color)
        player_tile_input = input('Please choose a tile to play.\n')
        print(Style.RESET_ALL)

        while not player_tile_input.isdigit() or int(player_tile_input) not in self.available_tiles:
            print(Fore.RED + f'Invalid input : {player_tile_input}' + Style.RESET_ALL)
            print(
                'Please choose a tile to play among values : ' + Fore.YELLOW + f'{self.available_tiles} \n' + Style.RESET_ALL)
            player_tile_input = input()

        print(f'Player Tile input is : {player_tile_input}')
        self.game_board[int(player_tile_input)] = selected_player.move_style
        self.available_tiles.pop(self.available_tiles.index(int(player_tile_input)))

    @staticmethod
    def ask_play_again():
        options = ('Y', 'N')
        while True:
            play_again_input = input('Do You want to play another game ? Y/N\n')
            if play_again_input.isdigit() or play_again_input.upper() not in options:
                print(f'Incorrect input, please choose an option from : {options}')
                continue
            else:
                break

        return play_again_input

    def reset_board(self):
        self.game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.available_tiles = list(range(1, 10))
