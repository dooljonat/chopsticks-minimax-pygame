from settings import Player, Hands, PLAYER_HANDS, COMPUTER_HANDS, ALL_HANDS, GameSettings, GameState

class Board:
    def get_init_board(self):
        _board = GameSettings.DEFAULT_BOARD.copy()
        return _board
    
    def is_valid_attack(self, current_board, indx, target_indx):
        if indx != target_indx:
            if current_board[indx] > 0 and current_board[target_indx] > 0:
                if indx in PLAYER_HANDS:
                    return target_indx in COMPUTER_HANDS
                if indx in COMPUTER_HANDS:
                    return target_indx in PLAYER_HANDS
        return False

    def is_valid_transfer(self, current_board, indx, target_indx, transfer_amount):
        if ((indx in PLAYER_HANDS and target_indx in PLAYER_HANDS) 
            or (indx in COMPUTER_HANDS and target_indx in COMPUTER_HANDS)):
            if current_board[indx] > 0 and current_board[target_indx] > 0:
                if transfer_amount < current_board[indx]:
                    if ((current_board[target_indx] + transfer_amount) <= 4
                         and (current_board[indx] - transfer_amount) > 0):
                         return True
        return False

    def is_valid_division(self, current_board, current_player):
        if current_player == Player.PLAYER:
            vals = [current_board[Hands.PLAYER_LEFT], current_board[Hands.PLAYER_RIGHT]]
            vals.sort()
            if vals[1] > 1 and vals[0] == 0:
                return True

        if current_player == Player.COMPUTER:
            vals = [current_board[Hands.COMPUTER_LEFT], current_board[Hands.COMPUTER_RIGHT]]
            vals.sort()
            if vals[1] > 1 and vals[0] == 0:
                return True

        return False

    def get_possible_board_states_after_turn(self, current_board, current_player):
        board_vals = [current_board[hand] for hand in ALL_HANDS]
        possible_board_states = []

        # TODO
        print(board_vals)

        return possible_board_states

    def make_move(self, current_board, current_player, indx, target_indx, move_type, transfer_amount=None):
        pass

    def update_board(self, current_board):
        # Update board, terminate hands

        _board = current_board.copy()

        for hand in ALL_HANDS:
            if current_board[hand] >= 5:
                current_board[hand] = 0
    
        return _board

    def get_game_state(self, current_board, current_turn_number):
        # Get game state

        # If game is in a draw (has been running for too many turns)
        if current_turn_number >= GameSettings.DEFAULT_TURNS_RESULTING_IN_DRAW:
            return GameState.DRAW
        else:
            # If player or computer won the game
            player_sum = 0
            for hand in PLAYER_HANDS:
                player_sum += current_board[hand]
            computer_sum = 0
            for hand in COMPUTER_HANDS:
                computer_sum += current_board[hand]

            if player_sum == 0:
                return GameState.COMPUTER_WON
            elif computer_sum == 0:
                return GameState.PLAYER_WON
            # If no player won
            else:
                return GameState.RUNNING

board_object = Board()

board = Board.get_init_board()
print(board)