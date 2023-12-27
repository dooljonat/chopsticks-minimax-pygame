from random import randint

class Game:
    current_turn = 1
    current_board = [1,1,1,1]

    player = 1
    player_indices = [0,1]

    computer = 2
    computer_indices = [2,3]

    def __init__(self):
        pass

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

    def check_state(self):
        # Returns 1 if player lost
        #           2 if computer lost
        #           0 if game is still running
        if self.current_board[0] == 0 and self.current_board[1] == 0:
            return 1
        elif self.current_board[2] == 0 and self.current_board[3] == 0:
            return 2
        else:
            return 0
        
    def terminate_hands(self):
        # Loops through game board,
        # Sets any index equal to zero if they hold a value > 5
        for indx in range(len(self.current_board)):
            if self.current_board[indx] >= 5:
                self.current_board[indx] = 0

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

            valid_move_made = self.update_board(player_hand_indx, opponent_hand_indx)

            if not valid_move_made:
                print("Please ensure you are picking a target hand that has not yet been elimnated! (e.g., value is 0)")

    def move_random_agent_computer(self):
        valid_move_made = False

        while not valid_move_made:
            computer_hand_moved = randint(2,3)
            player_hand_picked = randint(0,1)
        
            valid_move_made = self.update_board(computer_hand_moved, player_hand_picked)

#            if not valid_move_made:
#                print("Please ensure you are picking a target hand that has not yet been elimnated! (e.g., value is 0)")

    def move_minimax_agent_computer(self):
        pass

    def update_board(self, indx, target_indx):
        # Adds the value of the two indices together at the target index to
        # update the board after a move is made
        # Will return false if an invalid move is made (target_indx is zero and the hand no longer exists)
        if self.current_board[target_indx] > 0:
            self.current_board[target_indx] += self.current_board[indx]
            return True
        else:
            return False

    def split_hands(self, target_indices):
        # Splits the values of the indices down the middle if
        # One index is eliminated (value is zero)
        # The other index is an even, divisible number
        # Returns True if successful and False if not
        elim_indx = -1
        split_indx = -1
        for indx in target_indices:
            val = self.current_board[indx]

            if val == 0:
                elim_indx = indx
            if val > 0:
                if (val % 2) == 0:
                    split_indx = indx

        if ((elim_indx == -1) or (split_indx == -1) or (elim_indx == split_indx)):
            return False
        else:
            split_val = current_board[split_indx] / 2

            for _ in target_indices:
                self.current_board[_] = split_val
            return True
    

    def play(self):
        current_state = 0
        current_player = self.player
        current_turn = 1

        print("Welcome to finger chess game!\n")

        while current_state == 0:
            print("Currently on turn: " + str(current_turn) + "\n")
            self.print_board()

            # Player's turn
            if current_player == self.player:
                self.move_player()

                # Switch player
                current_player = self.computer

            # Computer's turn
            elif current_player == self.computer:
                print("\tComputer is making their move....\n\n")
                self.move_random_agent_computer()
                
                # Switch player
                current_player = self.player

            # Check state
            self.terminate_hands()
            current_state = self.check_state()
            
            current_turn += 1

        if current_state == 2:
            print("Player won!")
        elif current_state == 1:
            print("Computer won!")
            


            
            
            
