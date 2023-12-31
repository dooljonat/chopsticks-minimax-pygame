from random import randint, choice

from settings import GameSettings, GameState, Player
from mini_max_agent import MiniMax

class Game:
    def __init__(self,
                first_player=choice([Player.PLAYER, Player.COMPUTER]),
                board=GameSettings.DEFAULT_BOARD,
                num_turns_resulting_in_draw=GameSettings.DEFAULT_TURNS_RESULTING_IN_DRAW):
        self.current_board = board
        self.current_player = first_player
        self.current_turn = 1

        self.num_turns_resulting_in_draw = num_turns_resulting_in_draw

        self.minimax_agent = MiniMax(self)

    def print_hands(self, board, indices):
        _ = [1,2]
        hand = ""
        for board_indx,num in zip(indices, _):
            if board[board_indx] != 5:
                hand += "Hand " + str(num) + " : " + "'" + str(board[board_indx]) + "'" + " "
            else:
                hand += "Hand " + str(num) + " : " + "'" + "*" + "'" + " "
        return hand
   
    def print_board(self, board):
        print("Current hands are:")
        print("# Player's: ")
        print("# \t" + self.print_hands(board, GameSettings.PLAYER_INDICES))
        print("Computer's: ")
        print("# \t" + self.print_hands(board, GameSettings.COMPUTER_INDICES))
        print("\n")

    def check_state(self, board, current_turn_number):
        # If game won
        if (board[0] == 5 and board[1] == 5) or (board[2] == 5 and board[3] == 5):
            return GameState.GAME_OVER

        # If draw
        if current_turn_number >= self.num_turns_resulting_in_draw:
            return GameState.DRAW

        # If still running
        return GameState.RUNNING

    def get_winner(self, board, current_turn_number):
        if ((self.check_state(board, current_turn_number) == GameState.RUNNING)
            or (self.check_state(board, current_turn_number) ==  GameState.DRAW)):
            print("ERROR! get_winner() should only be called after check_state when game is terminated and not in a draw")
        else:
            if (board[0] == 5 and board[1] == 5):
                return Player.COMPUTER
            if (board[2] == 5 and board[3] == 5):
                return Player.PLAYER

    def terminate_hands(self, board):
        # Loops through game board,
        # Sets any index equal to five if they hold a value >= 5
        _board = board.copy()
        for indx in range(len(_board)):
            if _board[indx] >= 5:
                _board[indx] = 5
        return _board

    def move_player(self):
        valid_move_made = False

        while not valid_move_made:
            print("Your hands: ")
            print(self.print_hands(self.current_board, GameSettings.PLAYER_INDICES))

            player_hand_moved = input("\tWhich of your hands would you like to play?\n\tPlease enter either 1 or 2\n\tOr enter 0 to split hands\n\n")

            print("Opponent's hands: ")
            print(self.print_hands(self.current_board, GameSettings.COMPUTER_INDICES))
            opponent_hand_picked = input("\tWhich of the opponent's hands would you like to add to?\n\tPlease enter either 1 or 2\n\n")

            # Make move and add values together
            player_hand_indx = int(player_hand_moved)-1
            opponent_hand_indx = (int(opponent_hand_picked)-1)+2

            valid_move_made = self.is_valid_move(self.current_board, player_hand_indx, opponent_hand_indx)

            if not valid_move_made:
                print("Please ensure you are picking a target hand that has not yet been elimnated! (e.g., value is 0)")
            else:
                self.current_board = self.update_board(self.current_board, player_hand_indx, opponent_hand_indx)

    def move_random_agent_computer(self):
        valid_move_made = False

        while not valid_move_made:
            computer_hand_moved = randint(2,3)
            player_hand_picked = randint(0,1)
        
            valid_move_made = self.is_valid_move(self.current_board, computer_hand_moved, player_hand_picked)

            if valid_move_made:
                self.current_board = self.update_board(self.current_board, computer_hand_moved, player_hand_picked)

    def move_minimax_agent_computer(self, board, current_turn):
        move = self.minimax_agent.get_best_move(board, current_turn)

        # print("CURRENT BOARD: ", board)
        # print("MINIMAX SELECTED: ", move)

        if move == ["S"]:
            self.current_board = self.split_hands(board, GameSettings.COMPUTER_INDICES)
        else:
            self.current_board = self.update_board(board, move[0], move[1])

    def is_valid_move(self, board, indx, target_indx):
        return ((board[target_indx] < 5) 
            and (board[indx] < 5) 
            and (indx != target_indx) 
            and (((indx in GameSettings.PLAYER_INDICES) and (target_indx in GameSettings.COMPUTER_INDICES)) or ((indx in GameSettings.COMPUTER_INDICES) or (target_indx in GameSettings.PLAYER_INDICES))))

    def update_board(self, board, indx, target_indx):
        _board = board.copy()
        # Adds the value of the two indices together at the target index to
        # update the board after a move is made
        _board[target_indx] += _board[indx]
        return _board

    def is_valid_split(self, board, target_indices):
        vals = [board[i] for i in target_indices]
        vals.sort(reverse=True)
        return (len(set(vals)) != 1
                and (vals[0] == 5)
                and (vals[1] > 0)
                and (vals[1] % 2 == 0))

    def split_hands(self, board, target_indices):
        # Splits the values of the indices down the middle if
        # One index is eliminated (value is zero)
        # The other index is an even, divisible number
        # Returns True if successful and False if not
        _board = board.copy()

        vals = [_board[i] for i in target_indices]
        vals.sort()
        new_val = None
        if vals[0] == 2:
            new_val = 1
        else:
            new_val = vals[0]/2
        for indx in target_indices:
            _board[indx] = int(new_val)

        return _board
    
    def play_next_turn(self):
        print("Currently on turn: " + str(self.current_turn))
        self.print_board(self.current_board)

        # Player's turn
        if self.current_player == Player.PLAYER:
            self.move_player()

            # Switch player
            self.current_player = Player.COMPUTER

        # Computer's turn
        elif self.current_player == Player.COMPUTER:
            print("\tComputer is making their move....\n\n")
            self.move_minimax_agent_computer(self.current_board, current_turn=self.current_turn)
            
            # Switch player
            self.current_player = Player.PLAYER

        # Incr. current turn #
        self.current_turn += 1

        # Return current state after this turn
        self.current_board = self.terminate_hands(self.current_board)
        return self.check_state(self.current_board, self.current_turn)
