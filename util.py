from enum import Enum

class GameSettings():
    DEFAULT_BOARD = [1,1,1,1]

    PLAYER_INDICES = [0,1]
    COMPUTER_INDICES = [2,3]

    DEFAULT_TURNS_RESULTING_IN_DRAW=100

class MiniMaxSettings():
    MAX_LOOK_DEPTH = 10

class GameState(Enum):
    RUNNING = 0
    DRAW = 1
    GAME_OVER = 2

class Player(Enum):
    PLAYER = 1
    COMPUTER = 2
