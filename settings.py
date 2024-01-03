from enum import Enum

class GameSettings:
    DEFAULT_BOARD = [1,1,1,1]

    DEFAULT_TURNS_RESULTING_IN_DRAW=100

class Player(Enum):
    PLAYER = 0
    COMPUTER = 1

class Hands(Enum):
    PLAYER_LEFT = 0
    PLAYER_RIGHT = 1
    
    COMPUTER_LEFT = 0
    COMPUTER_RIGHT = 1

PLAYER_HANDS   = [Hands.PLAYER_LEFT, Hands.PLAYER_RIGHT]
COMPUTER_HANDS = [Hands.COMPUTER_LEFT, Hands.COMPUTER_RIGHT]
ALL_HANDS = [Hands.PLAYER_LEFT, Hands.PLAYER_RIGHT, Hands.COMPUTER_LEFT, Hands.COMPUTER_RIGHT]

class MoveType(Enum):
    ATTACK = 0
    TRANSFER = 1
    DIVISION = 2

class Moves:
    PLAYER_ATTACKS = [
        [Hands.PLAYER_LEFT, Hands.COMPUTER_LEFT],
        [Hands.PLAYER_LEFT, Hands.COMPUTER_RIGHT],
        [Hands.PLAYER_RIGHT, Hands.COMPUTER_LEFT],
        [Hands.PLAYER_RIGHT, Hands.COMPUTER_RIGHT],
    ]
    PLAYER_TRANSFERS = [
        [HANDS.PLAYER_LEFT, Hands.PLAYER_RIGHT],
        [HANDS.PLAYER_RIGHT, Hands.PLAYER_LEFT]
    ]

    COMPUTER_ATTACKS = [
        [Hands.COMPUTER_LEFT, Hands.PLAYER_LEFT],
        [Hands.COMPUTER_LEFT, Hands.PLAYER_RIGHT],
        [Hands.COMPUTER_RIGHT, Hands.PLAYER_LEFT],
        [Hands.COMPUTER_RIGHT, Hands.PLAYER_RIGHT],
    ]
    COMPUTER_TRANSFERS = [
        [Hands.COMPUTER_LEFT, Hands.COMPUTER_RIGHT],
        [Hands.COMPUTER_RIGHT, Hands.COMPUTER_LEFT]
    ]

class GameState(Enum):
    RUNNING = 0
    DRAW = 1
    PLAYER_WON = 2
    COMPUTER_WON = 3

# class Player(Enum):
#     PLAYER = 1
#     COMPUTER = 2
