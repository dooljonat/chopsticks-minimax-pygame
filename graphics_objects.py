import pygame

from settings import Hands
from display_settings import PygameSettings, ComputerSpritePaths, PlayerSpritePaths

# NOTE: All sprites use DEFAULT_POS because all sprites images are hardcoded to be 1280x720
#       and include their relative positions by default.
#       I decided to do this because I am lazy. 
#       This should be fixed when I muster the courage to confront my own shortcomings.

class Button:
    def __init__(self, screen, name, x, y, width, height, hover_image, on_click_function=None, is_active=False, already_clicked=False):
        self.name = name

        self.screen = screen

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Hover image and surface
        self.hover_image = pygame.image.load(hover_image).convert_alpha()
        self.hover_image_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
        # self.hover_image_surface = self.hover_image_surface.convert_alpha()
        self.hover_image_surface.blit(self.hover_image, PygameSettings.DEFAULT_POS)

        # Rect for collision detection purposes
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.on_click_function = on_click_function
        self.is_active = is_active
        self.already_clicked = already_clicked

    def handle(self):
        mousePos = pygame.mouse.get_pos()

        if self.is_active:
            print("uhhh im active")
            if self.buttonRect.collidepoint(mousePos):
                print("ermmm... i'm being hovered on now")
                self.screen.blit(self.hover_image_surface, PygameSettings.DEFAULT_POS)

                # Get if button was clicked on
                if pygame.mouse.get_pressed(num_buttons=3)[0]:

                    if not self.already_clicked:
                        # Call onClickFunction
                        self.onclickFunction()

class PlayerRightHandUISprite:
    pass

class ComputerLeftHandSprite:
    def __init__(self):
        self.palm_img = pygame.image.load(ComputerSpritePaths.left_hand_sprite_path).convert_alpha()
        self.thumb_img = pygame.image.load(ComputerSpritePaths.left_thumb_sprite_path).convert_alpha()

        self.pointer_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.left_pointer_paths]
        self.middle_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.left_middle_paths]
        self.ring_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.left_ring_paths]
        self.pinky_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.left_pinky_paths]

    def draw(self, screen, board):
        # Draw palm
        screen.blit(self.palm_img, PygameSettings.DEFAULT_POS)

        # Get current count of computer's left hand in-game
        hand_count = board[Hands.COMPUTER_LEFT]

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

class ComputerRightHandSprite:
    def __init__(self):
        self.palm_img = pygame.image.load(ComputerSpritePaths.right_hand_sprite_path).convert_alpha()
        self.thumb_img = pygame.image.load(ComputerSpritePaths.right_thumb_sprite_path).convert_alpha()

        self.pointer_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.right_pointer_paths]
        self.middle_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.right_middle_paths]
        self.ring_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.right_ring_paths]
        self.pinky_imgs = [pygame.image.load(path).convert_alpha() for path in ComputerSpritePaths.right_pinky_paths]

    def draw(self, screen, board):
        # Draw palm
        screen.blit(self.palm_img, PygameSettings.DEFAULT_POS)

        # Get current count of computer's right hand in-game
        hand_count = board[Hands.COMPUTER_RIGHT]

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

class ComputerSprite:
    def __init__(self):
        self.img = pygame.image.load(ComputerSpritePaths.computer_sprite_path).convert_alpha()

        self.left_hand = ComputerLeftHandSprite()
        self.right_hand = ComputerRightHandSprite()

    def draw(self, screen, board):
        # Draw self
        screen.blit(self.img, PygameSettings.DEFAULT_POS)

        # Draw left hand
        self.left_hand.draw(screen, board)

        # Draw right hand
        self.right_hand.draw(screen, board)

class PlayerLeftHandSprite():
    def __init__(self):
        self.palm_img = pygame.image.load(PlayerSpritePaths.left_hand_sprite_path).convert_alpha()
        self.thumb_img = pygame.image.load(PlayerSpritePaths.left_thumb_sprite_path).convert_alpha()

        self.pointer_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.left_pointer_paths]
        self.middle_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.left_middle_paths]
        self.ring_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.left_ring_paths]
        self.pinky_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.left_pinky_paths]

    def draw(self, screen, board):
        # Draw palm
        screen.blit(self.palm_img, PygameSettings.DEFAULT_POS)

        # Get current count of computer's right hand in-game
        hand_count = board[Hands.PLAYER_LEFT]

        # Draw fingers
        fingers_up = [0,0,0,0]

        if hand_count < 5:
            for i in range(hand_count):
                fingers_up[i] = 1
        fingers_up.reverse()

        for i, val in enumerate(fingers_up):
            if i == 3:
                screen.blit(self.pointer_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 2:
                screen.blit(self.middle_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 1:
                screen.blit(self.ring_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 0:
                screen.blit(self.pinky_imgs[val], PygameSettings.DEFAULT_POS)

        # Draw thumb
        screen.blit(self.thumb_img, PygameSettings.DEFAULT_POS)

class PlayerRightHandSprite:
    def __init__(self):
        self.palm_img = pygame.image.load(PlayerSpritePaths.right_hand_sprite_path).convert_alpha()
        self.thumb_img = pygame.image.load(PlayerSpritePaths.right_thumb_sprite_path).convert_alpha()

        self.pointer_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.right_pointer_paths]
        self.middle_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.right_middle_paths]
        self.ring_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.right_ring_paths]
        self.pinky_imgs = [pygame.image.load(path).convert_alpha() for path in PlayerSpritePaths.right_pinky_paths]

    def draw(self, screen, board):
        # Draw thumb
        screen.blit(self.thumb_img, PygameSettings.DEFAULT_POS)

        # Draw palm
        screen.blit(self.palm_img, PygameSettings.DEFAULT_POS)

        # Get current count of computer's right hand in-game
        hand_count = board[Hands.PLAYER_RIGHT]

        # Draw fingers
        fingers_up = [0,0,0,0]

        if hand_count < 5:
            for i in range(hand_count):
                fingers_up[i] = 1
        fingers_up.reverse()

        for i, val in enumerate(fingers_up):
            if i == 3:
                screen.blit(self.pointer_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 2:
                screen.blit(self.middle_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 1:
                screen.blit(self.ring_imgs[val], PygameSettings.DEFAULT_POS)
            if i == 0:
                screen.blit(self.pinky_imgs[val], PygameSettings.DEFAULT_POS)

class PlayerSprite:
    def __init__(self):
        self.left_hand = PlayerLeftHandSprite()
        self.right_hand = PlayerRightHandSprite()

    def draw(self, screen, board):
        self.left_hand.draw(screen, board)
        self.right_hand.draw(screen, board)
