import pygame
import random

from settings import GameState, Player, Hands
from display_settings import PygameSettings, ColorPalette
from graphics_objects import ComputerSprite, PlayerSprite, Button
from board import Board
from mini_max_agent import MiniMax
from display_settings import UISpritePaths

# Init pygame
pygame.init()

# -> Init screen
screen = pygame.display.set_mode((PygameSettings.SCREEN_WIDTH, PygameSettings.SCREEN_HEIGHT))
pygame.display.set_caption('finger chess')

# Init graphics objects
computer_sprite = ComputerSprite()
player_sprite   = PlayerSprite()


print("\n\n*****************************\nWelcome to finger chess game!\n*****************************\n")

# Init game
board = Board.get_init_board()
current_turn = 1
current_state = GameState.RUNNING
player_turn = random.choice([True, False])

# Init minimax agent
computer_agent = MiniMax()



# Create button selection handler functions
currently_selected_hand = None
currently_selected_target_hand = None
def select_p_left():
    currently_selected_hand = Hands.PLAYER_LEFT
def select_p_right():
    currently_selected_hand = Hands.PLAYER_RIGHT
def select_c_left():
    currently_selected_hand = Hands.COMPUTER_LEFT
def select_c_right():
    currently_selected_hand = Hands.COMPUTER_RIGHT

# Init UI objects
menu_bar_image = pygame.image.load(UISpritePaths.menu_bar)

# Init buttons
player_left_hand_button = Button(screen, "player_left", 302, 474, 200, 200, hover_image=UISpritePaths.player_left, on_click_function=select_p_left)

clock = pygame.time.Clock()

# main game loop
while current_state == GameState.RUNNING:
    # Draw graphics to screen
    screen.fill(ColorPalette.BACKGROUND_COLOR)
    computer_sprite.draw(screen, board)
    player_sprite.draw(screen, board)
    screen.blit(menu_bar_image, PygameSettings.DEFAULT_POS)

    # Handle button UI objects
    player_left_hand_button.handle()

    # Update display
    pygame.display.flip()

    # Get input
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    # Make move
    if player_turn:
        # Active player hand selection buttons
        player_left_hand_button.is_active = True

        # possible_board_states = Board.get_possible_board_states_after_turn(board, Player.PLAYER)

        # states = {i+1:state for i, state in enumerate(possible_board_states)}
        # print("Please pick your next move!")
        # for indx in states:
        #     print(f"\t{indx}: ", states[indx])

        # move = int(input())

        # board = states[move]

        if currently_selected_hand != None:
            player_turn = not player_turn
    else:
        print("Computer picking next move...")
        state = computer_agent.get_best_move(board, current_turn)
        print("\tComputer picked state ", state)

        board = state

        player_turn = not player_turn
        

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
    
    if current_state == GameState.PLAYER_WON:
        print("Player won the game!")

    if current_state == GameState.COMPUTER_WON:
        print("Computer won the game!")

    current_turn += 1

    clock.tick()
    print(clock.get_fps())