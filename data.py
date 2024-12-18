SCREEN_WIDTH: int = 810
SCREEN_HEIGHT: int = 740
FPS: int = 60

WINSCORE: int = 100

DEFAULT_BORDER_RADIUS: int = 50

FRAME_FEET_WIDTH: int = 40
FRAME_FEET_HEIGHT: int = 40
FRAME_MARGIN: int = 25

CIRCLE_DIAMETER: int = 100
CIRCLE_PADDING: int = 10

BUTTON_OUTLINE_WIDTH: int = 3
BUTTON_SHADOW_OFFSET: int = 20

FONT: str = "Resources/PixelFont.ttf"

columnBoundaries: dict[int, tuple[int, int]] = { }
for i in range(7):
    columnBoundaries[i] = (FRAME_MARGIN + ((CIRCLE_DIAMETER + CIRCLE_PADDING) * i)), (
                            FRAME_MARGIN + CIRCLE_DIAMETER) + ((CIRCLE_DIAMETER + CIRCLE_PADDING) * i)

mouseLeftclick: bool = False



#! Errors:
ERROR_COLUMN_FULL: str = "Column is full!"
ERROR_INVALID_COORDS: str = "Invalid coordinates!"
ERROR_INVALID_PLAYERID: str = "Invalid player ID!"



#? Colours:
player1Colour: tuple[int, int, int] = (190, 0, 0)
player2Colour: tuple[int, int, int] = (190, 190, 0)

USERCOLOURS: dict[int, tuple[int, int, int]] = {
    0: (190, 0, 0),
    1: (190, 100, 0),
    2: (190, 190, 0),
    3: (170, 0, 190),
    4: (220, 0, 120),
    5: (0, 190, 180),
    6: (0, 80, 190),
    7: (0, 120, 0),
    8: (0, 240, 0)
}

USERCOLOURID = {v: k for k, v in USERCOLOURS.items()}
ALREADY_PICKED_COLOUR: tuple[int, int, int] = (50, 50, 50)
USER_CHOSEN_OUTLINE_COLOUR: tuple[int, int, int] = (0, 120, 120)

TRANSPARENT_COLOUR: tuple[int, int, int, int] = (0, 0, 0, 0)

FRAME_COLOUR: tuple[int, int, int] = (50, 50, 200)
BACKGROUND_COLOUR: tuple[int, int, int] = (200, 200, 200)

ENDSCREEN_TEXT_COLOUR: tuple[int, int, int] = (255, 255, 255)
ENDSCREEN_COLOUR: tuple[int, int, int] = (0, 0, 0, 200)

BUTTON_COLOUR: tuple[int, int, int] = (150, 150, 255)
BUTTON_HOVER_COLOUR: tuple[int, int, int] = (100, 100, 200)
BUTTON_SHADOW_COLOUR: tuple[int, int, int, int] = (0, 0, 0, 50)
BUTTON_OUTLINE_COLOUR: tuple[int, int, int] = (0, 0, 0)
BUTTON_TEXT_COLOUR: tuple[int, int, int] = (20, 20, 20)

#* Window titles:
TITLE_GAME: str = "Connect 4 | Game"
TITLE_MENU: str = "Connect 4 | Main Page"
TITLE_COLOUR_PICKER: str = "Connect 4 | Colour Picker"