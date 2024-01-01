import copy
import math

from settings import GameSettings, BoardInfo, MiniMaxSettings, GameState, Player

class MiniMax:
    all_possible_computer_moves = [["S"], [2, 0], [2, 1], [3, 0], [3, 1]]
    all_possible_human_moves    = [["S"], [0, 2], [0, 3], [1, 2], [1, 3]]

    MAX_SCORE = 1000
    MIN_SCORE = -1000

    def __init__(self, game):
        self.game = game 

    def score_game(self, current_board, current_turn_number, current_depth, current_player):
        state = self.game.check_state(current_board, current_turn_number)
        current_score = 0

        if state == GameState.GAME_OVER:
            winner = self.game.get_winner(current_board, current_turn_number)
            current_score = self.MAX_SCORE-current_depth if winner == Player.COMPUTER else self.MIN_SCORE+current_depth
        else:
            player_vals = [current_board[0], current_board[1]]
            computer_vals = [current_board[2], current_board[3]]

            # Decentivize being in a state where you have one terminated
            # hand but can't split (other hand is an odd number)
            if 5 in current_board:
                if current_player == Player.PLAYER:
                    if (sum(player_vals)-5)%2 == 1:
                        current_score = (self.MAX_SCORE)*.75 - current_depth

                if current_player == Player.COMPUTER:
                    if (sum(computer_vals)-5)%2 == 1:
                        current_score = (self.MIN_SCORE)*.75 + current_depth

        return state, current_score

    def get_possible_moves(self, current_board, current_player):
        new_moves = []

        # Get moves available to computer/agentprint
        all_possible_moves = (self.all_possible_computer_moves if current_player == Player.COMPUTER 
            else self.all_possible_human_moves)
        player_indices = (BoardInfo.COMPUTER_INDICES if current_player == Player.COMPUTER
            else BoardInfo.PLAYER_INDICES)

        for move in all_possible_moves:
            if move[0] == "S":
                # Check if split is available
                if self.game.is_valid_split(current_board, player_indices):
                    new_moves += [move]
            else:
                # Check if either move indx or target indx is terminated (making move unavailable)
                if self.game.is_valid_move(current_board, move[0], move[1]):
                    new_moves += [move]

        # Return new moves
        return new_moves

    def minimax(self, current_board, last_known_turn_number, current_player, depth=0):
        # Init values
        current_turn_number = last_known_turn_number + depth
        current_player_indices = (BoardInfo.COMPUTER_INDICES if current_player == BoardInfo.PLAYER_INDICES 
            else BoardInfo.COMPUTER_INDICES)
        next_player = (Player.COMPUTER if current_player == Player.PLAYER 
            else Player.PLAYER)

        # Get current state and score of the game
        state, score = self.score_game(current_board, current_turn_number, depth, current_player)

        # Update depth 
        depth = depth + 1

        # If game is in a terminated state
        if (state == GameState.GAME_OVER
                or state == GameState.DRAW 
                or depth >= MiniMaxSettings.MAX_LOOK_DEPTH):
            return score

        # Get possible moves, and their respective score outcomes
        possible_score_outcomes = []
        possible_moves = self.get_possible_moves(current_board, current_player)

        for move in possible_moves:
            # Update the board to reflect the move
            _board = None
            if move == ["S"]:
                _board = self.game.split_hands(current_board, current_player_indices)
            else:
                _board = self.game.update_board(current_board, move[0], move[1])

            _board = self.game.terminate_hands(_board)

            # Get the score this move would lead to
            possible_score_outcomes.append(self.minimax(_board, last_known_turn_number, next_player, depth))
             

        print(current_turn_number)
        print(depth)
        possible_score_outcomes.sort()
        for outcome in possible_score_outcomes:
            print(possible_score_outcomes)
        print()

        # If our current goal is to maximize (current player is computer), return max
        # else, (current player is player), return min
        return (max(possible_score_outcomes, default=10) 
                if current_player == Player.COMPUTER 
                else min(possible_score_outcomes, default=0))

    def get_best_move(self, board, current_turn_number, current_player=Player.COMPUTER):
        bestScore = -math.inf
        bestMove = None

        for move in self.get_possible_moves(board, current_player):
            _board = None
            if move == ["S"]:
                _board = self.game.split_hands(board, BoardInfo.COMPUTER_INDICES)
            else:
                _board = self.game.update_board(board, move[0], move[1])
            score = self.minimax(_board, current_turn_number, False)
            if score != "EMPTY":
                if score > bestScore:
                    bestScore = score
                    bestMove  = move

        return bestMove