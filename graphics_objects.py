import pygame

from settings import GameSettings
from display_settings import PygameSettings, ComputerSpritePaths

# NOTE: All sprites use DEFAULT_POS because all sprites images are hardcoded to be 1280x720
#       and include their relative positions by default.
#       I decided to do this because I am lazy. 
#       This should be fixed when I muster the courage to confront my own shortcomings.

class PlayerUI:
    pass

class ComputerRightHand:
    def __init__(self):
        self.palm_img = pygame.image.load(ComputerSpritePaths.right_hand_sprite_path)
        self.thumb_img = pygame.image.load(ComputerSpritePaths.right_thumb_sprite_path)

        self.pointer_imgs = [pygame.image.load(path) for path in ComputerSpritePaths.right_pointer_paths]
        self.middle_imgs = [pygame.image.load(path) for path in ComputerSpritePaths.right_middle_paths]
        self.ring_imgs = [pygame.image.load(path) for path in ComputerSpritePaths.right_ring_paths]
        self.pinky_imgs = [pygame.image.load(path) for path in ComputerSpritePaths.right_pinky_paths]

    def draw(self, screen, game):
        # Draw palm
        screen.blit(self.palm_img, PygameSettings.DEFAULT_POS)

        # Get current count of computer's right hand in-game
        hand_count = game.current_board[GameSettings.COMPUTER_RIGHT_HAND]
        print(hand_count)

        # Draw fingers
        fingers_up = [0,0,0,0]

        if hand_count < 5:
            for i in range(hand_count):
                fingers_up[i] = 1

        for i, val in enumerate(fingers_up):
            if i == 0:
                screen.blit(self.pointer_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 1:
                screen.blit(self.middle_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 2:
                screen.blit(self.ring_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 3:
                screen.blit(self.pinky_imgs[val], PygameSettings.DEFAULT_POS)

        # Draw thumb
        screen.blit(self.thumb_img, PygameSettings.DEFAULT_POS)

class Computer:
    def __init__(self):
        self.img = pygame.image.load(ComputerSpritePaths.computer_sprite_path).convert_alpha()

        self.right_hand = ComputerRightHand()

    def draw(self, screen, game):
        # Draw self
        screen.blit(self.img, PygameSettings.DEFAULT_POS)

        # Draw right hand
        self.right_hand.draw(screen, game)
