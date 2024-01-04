import pygame
import random

from settings import GameState, Player
from display_settings import PygameSettings, ColorPalette
from graphics_objects import ComputerSprite, PlayerSprite
from board import Board
from mini_max_agent import MiniMax

# Init pygame
pygame.init()

# -> Init screen
screen = pygame.display.set_mode((PygameSettings.SCREEN_WIDTH, PygameSettings.SCREEN_HEIGHT))
pygame.display.set_caption('finger chess')

# Init graphics objects
computer_sprite = ComputerSprite()
player_sprite   = PlayerSprite()


print("\n\n*****************************\nWelcome to finger chess game!\n*****************************\n")

# TODO: I have become aware that chopsticks is actually a much more complicated
#       than the ruleset I was using https://en.wikipedia.org/wiki/Chopsticks_(hand_game)
#       Update ruleset accordingly using a maximum of 14 possible rules

# Init game
board = Board.get_init_board()
current_turn = 1
current_state = GameState.RUNNING
player_turn = random.choice([True, False])

# Init minimax agent
computer_agent = MiniMax()


# main game loop
while current_state == GameState.RUNNING:
    # Draw graphics to screen
    screen.fill(ColorPalette.BACKGROUND_COLOR)
    computer_sprite.draw(screen, board)
    player_sprite.draw(screen, board)

    # Update display
    pygame.display.flip()

    # Get input
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    # Make move
    if player_turn:
        possible_board_states = Board.get_possible_board_states_after_turn(board, Player.PLAYER)

        states = {i+1:state for i, state in enumerate(possible_board_states)}
        print("Please pick your next move!")
        for indx in states:
            print(f"\t{indx}: ", states[indx])

        move = int(input())

        board = states[move]

    else:
        print("Computer picking next move...")
        state = computer_agent.get_best_move(board, current_turn)
        print("\tComputer picked state ", state)

        board = state
        

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
    player_turn = not player_turn