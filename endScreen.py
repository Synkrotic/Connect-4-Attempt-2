import threading
import pygame as pg
from rectangle import Rectangle
from data import *
from button import Button
from pynput import mouse

class EndScreen:
    def __init__(self, winner: str, game: 'Game'): # type: ignore
        self.background: pg.Surface = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
        self.background.fill(ENDSCREEN_COLOUR)
        self.font: pg.font.Font = pg.font.Font(FONT, 64)
        self.game: 'Game' = game # type: ignore
        if winner == "tie": endText: str = "It's a tie!"
        else: endText: str = f"{winner} wins!"
        self.text: pg.Surface = self.font.render(endText, True, ENDSCREEN_TEXT_COLOUR)
        self.background.blit(self.text, (SCREEN_WIDTH // 2 - self.text.get_width() // 2, SCREEN_HEIGHT // 4))

        self.doneButton: Button = Button(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 8, SCREEN_WIDTH // 2 - SCREEN_WIDTH // 8, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 8, "Done", None)
        self.listener: mouse.Listener | None = None

        self.listenerThread: threading.Thread = threading.Thread(target=self.startMouseListener)
        self.listenerThread.start()


    def startMouseListener(self) -> None:
        """Start listening for mouse inputs.
            And updating the player when pressed."""
        self.listener = mouse.Listener(on_click=self.updateButton)
        self.listener.start()


    def updateButton(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        if not pg.mouse.get_focused(): return
        if not pressed or button != mouse.Button.left: return
        self.doneButton.logic()


    def update(self, screen: pg.display) -> None:
        screen.blit(self.background, (0, 0))
        self.doneButton.update(screen, self.game.leftClick)

        if self.doneButton.pressed:
            self.game.running = False