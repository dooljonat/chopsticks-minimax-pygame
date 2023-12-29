import copy
from game import Game

class MiniMax:
    all_possible_moves = [["S"], [2, 0], [2, 1], [3, 0], [3, 1]]

    def __init__(self, game, moves_to_look_forward_to=5):
        self.game = game 

    def score(self, current_board, turn_number):
        score = self.game.check_state(current_board, turn_number)
        # Computer won
        if score == 2:
            return 10
        # Player won
        elif score == 1:
            return -10
        else:
            return 0

    def get_possible_moves(self, current_board):
        possible_moves = copy.deepcopy(self.all_possible_moves)

        indices_to_remove = []
        # Check if split is available
        if not (self.game.is_valid_split(current_board, self.game.computer_indices)):
            indices_to_remove += [0]


        # If either the target or move hand is terminated, the move can't happen, so remove it'
        for i in range(1, len(possible_moves)):
            move = possible_moves[i]
        
            for indx in move:
                if current_board[indx] == 0:
                    indices_to_remove += [i]

        # Create new possible moveset
        new_moves = []
        for i in range(len(possible_moves)):
            if i not in indices_to_remove:
                new_moves += [possible_moves[i]]

        # Return new moves
        return new_moves

    def minimax(self, current_board, current_turn, look_depth, isMaximizing):
        score = self.score(current_board, current_turn+look_depth)

        # If game has been running too long (Draw)

        # If game was decided upon

        # If game is still running

        # If this is player's (minimizers) move

g = Game()
_ = MiniMax(g)
g.current_board = [1,3,2,0]
moves = _.get_possible_moves(g.current_board)
print(moves)


