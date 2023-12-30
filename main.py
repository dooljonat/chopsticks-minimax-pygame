import pygame

from util import GameState, Player
from game import Game

exited = False
finger_chess = Game()

print("\n\n*****************************\nWelcome to finger chess game!\n*****************************\n")

# main game loop
while not exited:
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