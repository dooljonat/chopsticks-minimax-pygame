import copy
import math

from settings import GameState, Player
from board import Board

class MiniMax:
    MAX_LOOK_DEPTH = 8

    def minimax(self, current_board, current_game_turn, computer_turn, depth=0):
        # Current search turn
        current_search_turn = current_game_turn + depth

        # Get current state
        state = Board.get_game_state(current_board, current_search_turn)

        # If game is in a terminated state
        if (state == GameState.COMPUTER_WON):
            return 100

        if (state == GameState.PLAYER_WON):
            return -100
        
        if (state == GameState.DRAW):
            return 0

        if (depth >= self.MAX_LOOK_DEPTH):
            return 0

        # If player is being maximized (computer)
        if computer_turn:
            bestScore = -1000

            possible_board_states = Board.get_possible_board_states_after_turn(current_board, Player.COMPUTER)
            for board in possible_board_states:
                score = self.minimax(board, current_game_turn, False, depth+1)
                print(f"\t\tdepth {depth} - score {score}")

                bestScore = max(score, bestScore)

            return bestScore

        # If player is being minimized (player)
        else:
            bestScore = 1000
            
            possible_board_states = Board.get_possible_board_states_after_turn(current_board, Player.PLAYER)
            for board in possible_board_states:
                score = self.minimax(board, current_game_turn, True, depth+1)
                bestScore = min(score, bestScore)

            return bestScore

    def get_best_move(self, board, current_turn_number):
        bestScore = -10_000
        bestState = None

        for board_state in Board.get_possible_board_states_after_turn(board, Player.COMPUTER):
            score = self.minimax(board, current_turn_number, True)
            if score > bestScore:
                bestScore = score
                bestState  = board_state

        return bestState