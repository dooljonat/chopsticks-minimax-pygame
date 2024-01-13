import pygame
import random

from settings import GameState, Player, Hands, PlayerTurnTypes
from display_settings import PygameSettings, ColorPalette
from graphics_objects import ComputerSprite, PlayerSprite, Button
from board import Board
from mini_max_agent import MiniMax
from sprite_paths import ComputerSpritePaths, PlayerSpritePaths, UISpritePaths

# Init pygame
pygame.init()

# -> Init screen
screen = pygame.display.set_mode((PygameSettings.SCREEN_WIDTH, PygameSettings.SCREEN_HEIGHT))
pygame.display.set_caption('finger chess')

# Init graphics objects
computer_sprite = ComputerSprite()
player_sprite   = PlayerSprite()

# Init game
board = Board.get_init_board()
current_turn = 1
current_state = GameState.RUNNING
player_turn = random.choice([True, False])

# Init minimax agent
computer_agent = MiniMax()

# Create button selection handler functions
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

# Init player input handler
player_input_handler = PlayerInputHandler()

# Init UI objects
menu_bar_image = pygame.image.load(UISpritePaths.menu_bar)
player_left_hand_button = Button(screen, "player_left", 302, 474, 200, 200, hover_image=UISpritePaths.player_left, on_click_function=player_input_handler.select_p_left)
player_right_hand_button = Button(screen, "player_right", 890, 474, 200, 200, hover_image=UISpritePaths.player_right, on_click_function=player_input_handler.select_p_right)
computer_left_hand_button = Button(screen, "computer_left", 350, 45, 200, 200, hover_image=UISpritePaths.computer_left, on_click_function=player_input_handler.select_c_left)
computer_right_hand_button = Button(screen, "computer_right", 1050, 45, 200, 200, hover_image=UISpritePaths.computer_right, on_click_function=player_input_handler.select_c_right)

clock = pygame.time.Clock()

print("\n\n*****************************\nWelcome to finger chess game!\n*****************************\n")

# main game loop
while current_state == GameState.RUNNING:
    # Draw graphics to screen
    screen.fill(ColorPalette.BACKGROUND_COLOR)
    computer_sprite.draw(screen, board)
    player_sprite.draw(screen, board)
    screen.blit(menu_bar_image, PygameSettings.DEFAULT_POS)

    # Handle button UI objects
    player_left_hand_button.handle()
    player_right_hand_button.handle()
    computer_left_hand_button.handle()
    computer_right_hand_button.handle()

    # Update display
    pygame.display.flip()

    # Get input
    for e in pygame.event.get():
        # If the last turn was a player transfer, get keyboard input to see if player presses ENTER,
        # if so, end the turn
        if player_turn and player_input_handler.last_turn_type == PlayerTurnTypes.IS_TRANSFERRING:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    player_input_handler.finished_turn = True

        # User quit the game
        if e.type == pygame.QUIT:
            pygame.quit()

    # Make move
    if player_turn:

        print(player_input_handler.last_turn_type)
        print(player_input_handler.turn_type)
        print(player_input_handler.selected_hand)
        print(player_input_handler.selected_target_hand)

        # Player hand selection buttons
        if board[Hands.PLAYER_LEFT] != 0:
            player_left_hand_button.is_active = True
        
        if board[Hands.PLAYER_RIGHT] != 0:
            player_right_hand_button.is_active = True

        # Player selected a target hand
        if player_input_handler.selected_hand != -1:
            # Activate computer buttons
            computer_left_hand_button.is_active = True
            computer_right_hand_button.is_active = True

            # If player hasn't decided what type of move they're making yet
            if not player_input_handler.turn_type:
                # Player selected own hand
                if player_input_handler.selected_target_hand in [Hands.PLAYER_LEFT, Hands.PLAYER_RIGHT]:
                    player_input_handler.turn_type = PlayerTurnTypes.IS_TRANSFERRING
                
                # Player selected computer hand
                if player_input_handler.selected_target_hand in [Hands.COMPUTER_LEFT, Hands.COMPUTER_RIGHT]:
                    player_input_handler.turn_type = PlayerTurnTypes.IS_ATTACKING

            # If player is attacking computer
            if player_input_handler.turn_type == PlayerTurnTypes.IS_ATTACKING:
                # Update board
                board[player_input_handler.selected_target_hand] += board[player_input_handler.selected_hand]

                # Finish turn
                player_input_handler.finished_turn = True

            # If player is transferring
            if player_input_handler.turn_type == PlayerTurnTypes.IS_TRANSFERRING:
                # Update board
                board[player_input_handler.selected_target_hand] += 1
                board[player_input_handler.selected_hand] -= 1

                # Reset input handler
                player_input_handler.reset()

        if player_input_handler.finished_turn:
            player_input_handler.reset()

            player_left_hand_button.is_active = False
            player_right_hand_button.is_active = False
            computer_left_hand_button.is_active = False
            computer_right_hand_button.is_active = False

            player_turn = not player_turn
            current_turn += 1
    else:
        print("Computer picking next move...")
        state = computer_agent.get_best_move(board, current_turn)
        print("\tComputer picked state ", state)

        board = state

        player_turn = not player_turn
        current_turn += 1
        

    print("\n\n")

    # Update game
    board = Board.update_board(board)
    current_state = Board.get_game_state(board, current_turn)

    print(board)
    print(current_state)

    # If game was terminated
    if current_state == GameState.DRAW:
        print("Twas a draw!")
        exited = True
    
    # If game was won
    if current_state == GameState.PLAYER_WON:
        print("Player won the game!")

    if current_state == GameState.COMPUTER_WON:
        print("Computer won the game!")

    clock.tick()
    print(clock.get_fps())
    print(pygame.mouse.get_pos())