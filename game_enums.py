from enum import Enum

class Player(Enum):
    PLAYER = 0
    COMPUTER = 1

class PlayerTurnTypes(Enum):
    IS_ATTACKING = 0
    IS_TRANSFERRING = 1

class Hands:
    PLAYER_LEFT = 0
    PLAYER_RIGHT = 1
    
    COMPUTER_LEFT = 2
    COMPUTER_RIGHT = 3

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
        [Hands.PLAYER_LEFT, Hands.PLAYER_RIGHT],
        [Hands.PLAYER_RIGHT, Hands.PLAYER_LEFT]
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
