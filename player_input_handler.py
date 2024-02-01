from game_enums import Hands

class PlayerInputHandler:
    last_turn_type = None
    turn_type = None

    selected_hand = -1
    selected_target_hand = -1
    finished_turn = False

    def select_p_left(self):
        if self.selected_hand == -1:
            self.selected_hand = Hands.PLAYER_LEFT
        else:
            if self.selected_hand != Hands.PLAYER_LEFT:
                self.selected_target_hand = Hands.PLAYER_LEFT

    def select_p_right(self):
        if self.selected_hand == -1:
            self.selected_hand = Hands.PLAYER_RIGHT
        else:
            if self.selected_hand != Hands.PLAYER_RIGHT:
                self.selected_target_hand = Hands.PLAYER_RIGHT

    def select_c_left(self):
        if self.selected_hand != -1:
            self.selected_target_hand = Hands.COMPUTER_LEFT

    def select_c_right(self):
        if self.selected_hand != -1:
            self.selected_target_hand = Hands.COMPUTER_RIGHT
    
    def reset(self):
        self.last_turn_type = self.turn_type
        self.turn_type = None
        self.selected_hand = -1
        self.selected_target_hand = -1
        self.finished_turn = False