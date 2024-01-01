import pygame

from settings import GameState, Player
from display_settings import PygameSettings, ColorPalette
from graphics_objects import ComputerSprite, PlayerSprite
from game import Game

# Init game
exited = False
finger_chess = Game()

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

# main game loop
while not exited:
    # Draw graphics to screen
    screen.fill(ColorPalette.BACKGROUND_COLOR)
    computer_sprite.draw(screen, finger_chess)
    player_sprite.draw(screen, finger_chess)

    # Update display
    pygame.display.flip()

    # Get input
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    # Play next turn
    current_state = finger_chess.play_next_turn()

    # If game was terminated
    if current_state == GameState.DRAW:
        print("Twas a draw!")
        exited = True
    
    if current_state == GameState.GAME_OVER:
        winner = finger_chess.get_winner(finger_chess.current_board, finger_chess.current_turn)
        _ = "Computer" if winner == Player.COMPUTER else "Player"
        print(f"{_} won the game!")
        exited = True