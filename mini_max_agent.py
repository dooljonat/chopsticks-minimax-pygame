import copy
import math

from settings import GameSettings, BoardInfo, MiniMaxSettings, GameState, Player

class MiniMax:
    all_possible_computer_moves = [["S"], [2, 0], [2, 1], [3, 0], [3, 1]]
    all_possible_human_moves    = [["S"], [0, 2], [0, 3], [1, 2], [1, 3]]

    MAX_SCORE = 10
    MIN_SCORE = -10

    def __init__(self, game):
        self.game = game 

    def score_game(self, current_board, current_turn_number, current_depth, current_player):
        state = self.game.check_state(current_board, current_turn_number)
        current_score = 0

        if state == GameState.GAME_OVER:
            winner = self.game.get_winner(current_board, current_turn_number)
            current_score = self.MAX_SCORE if winner == Player.COMPUTER else self.MIN_SCORE
        # else:
        #     # Incentivize player who got back to init state of 1 on left 1 on right
        #     if not (sum(current_board) == 4 and len(set(current_board)) == 1):
        #         if (current_board[BoardInfo.PLAYER_LEFT_HAND] == 1 
        #             and current_board[BoardInfo.PLAYER_RIGHT_HAND] == 1):
        #             current_score = self.MIN_SCORE+1
        #         if (current_board[BoardInfo.COMPUTER_LEFT_HAND] == 1 
        #             and current_board[BoardInfo.COMPUTER_RIGHT_HAND] == 1):
        #             current_score = self.MAX_SCORE-1

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

        # Get current state and score of the game
        state, score = self.score_game(current_board, current_turn_number, depth, current_player)

        print("depth: ", depth)
        print("virtual turn number: ", current_turn_number)

        # If game is in a terminated state
        if (state == GameState.GAME_OVER
                or state == GameState.DRAW 
                or depth >= MiniMaxSettings.MAX_LOOK_DEPTH):
            print("found terminated state: ", state)
            
            return score

        # If maximizing (computer)
        if current_player == Player.COMPUTER:
            bestScore = -1000

            possible_moves = self.get_possible_moves(current_board, current_player)

            print("maximizing computer")
            for move in possible_moves:
                _board = current_board.copy()
                _board = self.game.update_board(_board, move[0], move[1])
                _board = self.game.terminate_hands(_board)

                score = self.minimax(current_board, last_known_turn_number, Player.PLAYER, depth+1)
                bestScore = max(bestScore, score)

                print("\t", move, bestScore)

            return bestScore

        # If minimizing (player)
        if current_player == Player.PLAYER:
            bestScore = 1000

            possible_moves = self.get_possible_moves(current_board, current_player)

            print("minimizing player")
            for move in possible_moves:
                _board = current_board.copy()
                _board = self.game.update_board(_board, move[0], move[1])
                _board = self.game.terminate_hands(_board)
                score = self.minimax(current_board, last_known_turn_number, Player.COMPUTER, depth+1)
                bestScore = min(bestScore, score)

                print("\t", move, bestScore)

            return bestScore

    def get_best_move(self, board, current_turn_number, current_player=Player.COMPUTER):
        bestScore = -math.inf
        bestMove = None

        for move in self.get_possible_moves(board, current_player):
            _board = None
            if move == ["S"]:
                _board = self.game.split_hands(board, BoardInfo.COMPUTER_INDICES)
            else:
                _board = self.game.update_board(board, move[0], move[1])
            score = self.minimax(board, current_turn_number, current_player)
            if score != "EMPTY":
                if score > bestScore:
                    bestScore = score
                    bestMove  = move

        return bestMove