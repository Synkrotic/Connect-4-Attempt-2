import pygame as pg
from rectangle import Rectangle
from data import *
from pynput import mouse

class Button:
    def __init__(self, width: int, height: int, x: int, y: int, text: str, borderRadius: int | None):
        self.width: int = width
        self.height: int = height
        self.x = x
        self.y = y
        self.coords: tuple[int, int] = (self.x, self.y)
        self.text: str = text
        self.borderRadius = borderRadius if borderRadius != None else DEFAULT_BORDER_RADIUS
        self.font: pg.font.Font = pg.font.Font(FONT, 32)
        self.text: pg.Surface = self.font.render(self.text, True, BUTTON_TEXT_COLOUR)
        self.hovered: bool = False
        self.pressed: bool = False

        self.collider: dict[str, tuple[int, int]] = {
            "topLeft": (self.x, self.y),
            "topRight": (self.x + self.width, self.y),
            "center": (self.x + self.width // 2, self.y + self.height // 2),
            "bottomLeft": (self.x, self.y + self.height),
            "bottomRight": (self.x + self.width, self.y + self.height)
        }

        self.backgroundRect: Rectangle = Rectangle(self.width - BUTTON_OUTLINE_WIDTH * 2, self.height - BUTTON_OUTLINE_WIDTH * 2, self.x + BUTTON_OUTLINE_WIDTH, self.y + BUTTON_OUTLINE_WIDTH, BUTTON_COLOUR, self.borderRadius)
        self.outlineRect: Rectangle = Rectangle(self.width, self.height, self.x, self.y, BUTTON_OUTLINE_COLOUR, self.borderRadius)
        self.shadowRect: Rectangle = Rectangle(self.width, self.height, self.x + BUTTON_SHADOW_OFFSET, self.y + BUTTON_SHADOW_OFFSET, BUTTON_SHADOW_COLOUR, self.borderRadius)


    def update(self, screen: pg.display, leftClick: bool) -> None:
        self.hover()
        self.draw(screen)


    def hover(self) -> None:
        mouseCoords: tuple[int, int] = pg.mouse.get_pos()
        if (self.collider["topLeft"][0] <= mouseCoords[0] <= self.collider["topRight"][0]) and (
            self.collider["topLeft"][1] <= mouseCoords[1] <= self.collider["bottomLeft"][1]):
            self.hovered = True
            self.backgroundRect.image.fill(BUTTON_HOVER_COLOUR)
        else:
            self.hovered = False
            self.backgroundRect.image.fill(self.backgroundRect.colour)
        self.backgroundRect.doBorderRadius()


    def logic(self) -> None:
        if not self.hovered: return
        self.pressed = not self.pressed


    def drawText(self, screen: pg.display) -> None:
        textRect: pg.Rect = self.text.get_rect()
        textRect.center = self.collider["center"]
        screen.blit(self.text, textRect)

    
    def draw(self, screen: pg.display) -> None:
        self.shadowRect.draw(screen)
        self.outlineRect.draw(screen)
        self.backgroundRect.draw(screen)
        self.drawText(screen)