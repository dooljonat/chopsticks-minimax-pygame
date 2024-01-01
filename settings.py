from enum import Enum

class GameSettings:
    DEFAULT_BOARD = [1,1,1,1]

    DEFAULT_TURNS_RESULTING_IN_DRAW=100

class BoardInfo:
    PLAYER_INDICES = [0,1]
    COMPUTER_INDICES = [2,3]

    PLAYER_LEFT_HAND = 0
    PLAYER_RIGHT_HAND = 1

    COMPUTER_LEFT_HAND = 2
    COMPUTER_RIGHT_HAND = 3

class MiniMaxSettings:
    MAX_LOOK_DEPTH = 10

class GameState(Enum):
    RUNNING = 0
    DRAW = 1
    GAME_OVER = 2

class Player(Enum):
    PLAYER = 1
    COMPUTER = 2
