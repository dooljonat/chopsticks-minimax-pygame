

class MiniMax:
    def __init__(self, moves_to_look_forward_to=5):
        self.move_to_look_forward_to = moves_to_look_forward_to

    def minimax(self, current_board, depth, isCurrentMaximizingAgent):
        
        if current board is won or lost:
            return state
