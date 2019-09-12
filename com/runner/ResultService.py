class ResultService:
    winning_combinations = ((1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 6, 9), (3, 5, 7), (4, 5, 6), (7, 8, 9))

    def __init__(self, player_1, player_2):
        self.win_evaluation_result = False
        self.winning_player = None
        self.winning_row = []
        self.player_1 = player_1
        self.player_2 = player_2

    def check_winner(self, game_board):
        for combo in self.winning_combinations:
            if game_board[combo[0]] != ' ' \
                    and game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]]:
                self.winning_row = list(combo)
                self.win_evaluation_result = True

    def determine_winner(self, game_board):

        if len(self.winning_row) == 0:
            return

        if game_board[self.winning_row[0]] == self.player_1.move_style:
            self.winning_player = self.player_1
        else:
            self.winning_player = self.player_2
