from settings import Player, Hands, PLAYER_HANDS, COMPUTER_HANDS, ALL_HANDS, GameSettings, GameState, Moves, MoveType

class Board:
    def get_init_board():
        _board = GameSettings.DEFAULT_BOARD.copy()
        return _board
    
    def is_valid_attack(current_board, current_player, indx, target_indx):
        if indx != target_indx:
            if current_player == Player.PLAYER:
                if (indx not in PLAYER_HANDS or target_indx not in COMPUTER_HANDS):
                    return False
            if current_player == Player.COMPUTER:
                if (indx not in COMPUTER_HANDS or target_indx not in PLAYER_HANDS):
                    return False

            if current_board[indx] > 0 and current_board[target_indx] > 0:
                if indx in PLAYER_HANDS:
                    return target_indx in COMPUTER_HANDS
                if indx in COMPUTER_HANDS:
                    return target_indx in PLAYER_HANDS
        return False

    def is_valid_transfer(current_board, indx, target_indx, transfer_amount):
        if ((indx in PLAYER_HANDS and target_indx in PLAYER_HANDS) 
            or (indx in COMPUTER_HANDS and target_indx in COMPUTER_HANDS)):
            if transfer_amount < current_board[indx]:
                if ((current_board[target_indx] + transfer_amount) < 4
                        and (current_board[indx] - transfer_amount) > 0):
                        return True
        return False

    def get_possible_board_states_after_turn(current_board, current_player):
        board_vals = [current_board[hand] for hand in ALL_HANDS]
        possible_board_states = []

        if current_player == Player.PLAYER:
            # Get possible attacks
            for attack in Moves.PLAYER_ATTACKS:
                if Board.is_valid_attack(current_board, current_player, attack[0], attack[1]):
                    _board = current_board.copy()
                    _board[attack[1]] += _board[attack[0]]
                    _board = Board.update_board(_board)
                    possible_board_states += [_board]

            # Get possible transfers
            for transfer in Moves.PLAYER_TRANSFERS:
                for possible_transfer_amount in range(1, current_board[transfer[0]]):
                    if Board.is_valid_transfer(current_board, transfer[0], transfer[1], possible_transfer_amount):
                        _board = current_board.copy()
                        _board[transfer[1]] += possible_transfer_amount
                        _board[transfer[0]] -= possible_transfer_amount
                        _board = Board.update_board(_board)
                        possible_board_states += [_board]

        if current_player == Player.COMPUTER:
            # Get possible attacks
            for attack in Moves.COMPUTER_ATTACKS:
                if Board.is_valid_attack(current_board, current_player, attack[0], attack[1]):
                    _board = current_board.copy()
                    _board[attack[1]] += _board[attack[0]]
                    _board = Board.update_board(_board)
                    possible_board_states += [_board]

            # Get possible transfers
            for transfer in Moves.COMPUTER_ATTACKS:
                for possible_transfer_amount in range(1, current_board[transfer[0]]):
                    if Board.is_valid_transfer(current_board, transfer[0], transfer[1], possible_transfer_amount):
                        _board = current_board.copy()
                        _board[transfer[1]] += possible_transfer_amount
                        _board[transfer[0]] -= possible_transfer_amount
                        _board = Board.update_board(_board)
                        possible_board_states += [_board]
                    
        return possible_board_states

    def make_move(current_board, current_player, indx, target_indx, move_type, transfer_amount=None):
        _board = current_board.copy()

        if move_type == MoveType.ATTACK:
            if Board.is_valid_attack(_board, current_player, indx, target_indx):
                _board[target_indx] += _board[indx]

        if move_type == MoveType.TRANSFER:
            if Board.is_valid_transfer(_board, indx, target_indx, transfer_amount):
                _board[target_indx] += transfer_amount
                _board[indx] -= transfer_amount

        return _board

    def update_board(current_board):
        # Update board, terminate hands
        _board = current_board.copy()

        for hand in ALL_HANDS:
            if _board[hand] >= 5:
                _board[hand] = 0
    
        return _board

    def get_game_state(current_board, current_turn_number):
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
