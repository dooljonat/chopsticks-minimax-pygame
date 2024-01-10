_finger_names = ["pointer", "middle", "ring", "pinky"]
_finger_types = ["closed", "open"]

class PygameSettings:
    SCREEN_WIDTH  = 1280
    SCREEN_HEIGHT = 720

    DEFAULT_POS = (0,0)

class ColorPalette:
    BACKGROUND_COLOR = (246, 232, 224)

class ComputerSpritePaths:
    computer_sprite_path = "img/computer/computer_sprite.png"

    left_hand_path_stem = "img/computer/hands/left/"

    left_hand_sprite_path  = left_hand_path_stem + "computer_left_hand.png"
    left_thumb_sprite_path = left_hand_path_stem + "computer_left_thumb.png"

    left_pointer_paths = [left_hand_path_stem + "fingers/pointer/closed.png",
                            left_hand_path_stem + "fingers/pointer/open.png"]

    left_middle_paths = [left_hand_path_stem + "fingers/middle/closed.png",
                            left_hand_path_stem + "fingers/middle/open.png"]

    left_ring_paths = [left_hand_path_stem + "fingers/ring/closed.png",
                            left_hand_path_stem + "fingers/ring/open.png"]

    left_pinky_paths = [left_hand_path_stem + "fingers/pinky/closed.png",
                            left_hand_path_stem + "fingers/pinky/open.png"]

    right_hand_path_stem = "img/computer/hands/right/"

    right_hand_sprite_path  = right_hand_path_stem + "computer_right_hand.png"
    right_thumb_sprite_path = right_hand_path_stem + "computer_right_thumb.png"

    right_pointer_paths = [right_hand_path_stem + "fingers/pointer/closed.png",
                            right_hand_path_stem + "fingers/pointer/open.png"]

    right_middle_paths = [right_hand_path_stem + "fingers/middle/closed.png",
                            right_hand_path_stem + "fingers/middle/open.png"]

    right_ring_paths = [right_hand_path_stem + "fingers/ring/closed.png",
                            right_hand_path_stem + "fingers/ring/open.png"]

    right_pinky_paths = [right_hand_path_stem + "fingers/pinky/closed.png",
                            right_hand_path_stem + "fingers/pinky/open.png"]

class PlayerSpritePaths:
    left_hand_path_stem = "img/player/hands/left/"

    left_hand_sprite_path  = left_hand_path_stem + "player_left_hand.png"
    left_thumb_sprite_path = left_hand_path_stem + "player_left_thumb.png"

    left_pointer_paths = [left_hand_path_stem + "fingers/pointer/closed.png",
                            left_hand_path_stem + "fingers/pointer/open.png"]

    left_middle_paths = [left_hand_path_stem + "fingers/middle/closed.png",
                            left_hand_path_stem + "fingers/middle/open.png"]

    left_ring_paths = [left_hand_path_stem + "fingers/ring/closed.png",
                            left_hand_path_stem + "fingers/ring/open.png"]

    left_pinky_paths = [left_hand_path_stem + "fingers/pinky/closed.png",
                            left_hand_path_stem + "fingers/pinky/open.png"]

    right_hand_path_stem = "img/player/hands/right/"

    right_hand_sprite_path  = right_hand_path_stem + "player_right_hand.png"
    right_thumb_sprite_path = right_hand_path_stem + "player_right_thumb.png"

    right_pointer_paths = [right_hand_path_stem + "fingers/pointer/closed.png",
                            right_hand_path_stem + "fingers/pointer/open.png"]

    right_middle_paths = [right_hand_path_stem + "fingers/middle/closed.png",
                            right_hand_path_stem + "fingers/middle/open.png"]

    right_ring_paths = [right_hand_path_stem + "fingers/ring/closed.png",
                            right_hand_path_stem + "fingers/ring/open.png"]

    right_pinky_paths = [right_hand_path_stem + "fingers/pinky/closed.png",
                            right_hand_path_stem + "fingers/pinky/open.png"]

class UISpritePaths:
    menu_bar = "img/ui/menu_bar.png"

    player_left = "img/ui/player_hand_pointers/player_left.png"