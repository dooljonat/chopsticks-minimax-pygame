from random import randint
from enum import Enum

class GameState(Enum):
    RUNNING = 0
    DRAW = 1
    GAME_OVER = 2

class Player(Enum):
    PLAYER = 1
    COMPUTER = 2

class Game:
    current_turn = 1
    current_board = [1,1,1,1]

    player_indices = [0,1]
    computer_indices = [2,3]

    num_turns_resulting_in_draw = None    

    def __init__(self, num_turns_resulting_in_draw=25):
        self.num_turns_resulting_in_draw = num_turns_resulting_in_draw

    def print_hands(self, indices):
        _ = [1,2]
        hand = ""
        for board_indx,num in zip(indices, _):
            hand += "Hand " + str(num) + " : " + "'" + str(self.current_board[board_indx]) + "'" + " "
        return hand
   
    def print_board(self):
        print("Current hands are:")
        print("# Player's: ")
        print("# \t" + self.print_hands(self.player_indices))
        print("Computer's: ")
        print("# \t" + self.print_hands(self.computer_indices))
        print("\n")

    def check_state(self, board, current_turn_number):
        # If draw
        if current_turn_number > self.num_turns_resulting_in_draw:
            return GameState.DRAW
        else:
            # If game was won
            if (board[0] == 0 and board[1] == 0) or (board[2] == 0 and board[3] == 0):
                return GameState.GAME_OVER
            # If game running
            else:
                return GameState.RUNNING

    def get_winner(self, board, current_turn_number):
        if ((self.check_state(board, current_turn_number) == GameState.RUNNING)
            or (self.check_state(board, current_turn_number) ==  GameState.DRAW)):
            print("ERROR! get_winner() should only be called after check_state when game is terminated and not in a draw")
        else:
            if (board[0] == 0 and board[1] == 0):
                return Player.COMPUTER
            if (board[2] == 0 and board[3] == 0):
                return Player.PLAYER

    def terminate_hands(self, board):
        # Loops through game board,
        # Sets any index equal to zero if they hold a value > 5
        for indx in range(len(board)):
            if board[indx] >= 5:
                board[indx] = 0
        return board

    def move_player(self):
        valid_move_made = False

        while not valid_move_made:
            print("Your hands: ")
            print(self.print_hands(self.player_indices))

            player_hand_moved = input("\tWhich of your hands would you like to play?\n\tPlease enter either 1 or 2\n\tOr enter 0 to split hands\n\n")

            print("Opponent's hands: '")
            print(self.print_hands(self.computer_indices))
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

    def move_minimax_agent_computer(self):
        pass

    def is_valid_move(self, board, indx, target_indx):
        return ((board[target_indx] > 0) 
            and (board[indx] > 0) 
            and (indx != target_indx) 
            and (((indx in self.player_indices) and (target_indx in self.computer_indices)) or ((indx in self.computer_indices) or (target_indx in self.player_indices))))

    def update_board(self, board, indx, target_indx):
        # Adds the value of the two indices together at the target index to
        # update the board after a move is made
        board[target_indx] += board[indx]
        return board

    def is_valid_split(self, board, target_indices):
        vals = [board[i] for i in target_indices]
        vals.sort()
        return ((vals[0] == 0)
                and (vals[1] > 0)
                and (vals[1] % 2 == 0))

    def split_hands(self, board, target_indices):
        # Splits the values of the indices down the middle if
        # One index is eliminated (value is zero)
        # The other index is an even, divisible number
        # Returns True if successful and False if not
        vals = [board[i] for i in target_indices]
        vals.sort()
        new_val = vals[1]/2
        for indx in target_indices:
            board[indx] = new_val

        return board
    

    def play(self):
        current_state = GameState.RUNNING
        current_player = Player.PLAYER
        current_turn = 1

        print("Welcome to finger chess game!\n")

        while current_state == GameState.RUNNING:
            print("Currently on turn: " + str(current_turn) + "\n")
            self.print_board()

            # Player's turn
            if current_player == Player.PLAYER:
                self.move_player()

                # Switch player
                current_player = Player.COMPUTER

            # Computer's turn
            elif current_player == Player.COMPUTER:
                print("\tComputer is making their move....\n\n")
                self.move_random_agent_computer()
                
                # Switch player
                current_player = Player.PLAYER

            # Check state
            self.current_board = self.terminate_hands(self.current_board)
            current_state = self.check_state(self.current_board, current_turn)
            
            current_turn += 1

        if current_state == GameState.DRAW:
            print("Game was a tie!")
        else:
            _ = self.get_winner(self.current_board, current_turn)
            if _ == Player.PLAYER:
                print("You won!")
            if _ ==  Player.COMPUTER:
                print("Computer won!")
