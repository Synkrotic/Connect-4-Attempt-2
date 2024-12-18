import pygame as pg, threading
from board import Board
from player import Player
from pynput import mouse
from data import *
from aiplayer import AIPlayer
from endScreen import EndScreen

class Game:
    def __init__(self, ai: bool):
        self.board: Board = Board(6, 7)
        self.turn: bool = True
        self.running: bool = True
        self.ended: bool = False
        self.ai: bool = ai

        pg.init()
        pg.font.init()
        self.screen: pg.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
        pg.display.set_caption(TITLE_GAME)
        self.clock: pg.time.Clock = pg.time.Clock()

        self.player1: Player = Player(self, 1)
        self.player2: Player | AIPlayer
        if not self.ai: self.player2: Player = Player(self, 2)
        else: self.player2 = AIPlayer(self, 2)

        self.endScreen: EndScreen | None = None
        self.listener: mouse.Listener | None = None

        self.listenerThread: threading.Thread = threading.Thread(target=self.startMouseListener)
        self.listenerThread.start()


    def startMouseListener(self) -> None:
        """Start listening for mouse inputs.
            And updating the player when pressed."""
        self.listener = mouse.Listener(on_click=self.updatePlayer)
        self.listener.start()


    def updatePlayer(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        """Update the player based on the mouse input."""
        if not pg.mouse.get_focused() or self.ended: return
        if not pressed or button != mouse.Button.left: return

        if self.turn:
            self.player1.update()
        else:
            if not self.ai: self.player2.update()


    def update(self) -> None:
        if self.ended:
            self.endScreen.update(self.screen)
            return

        if self.ai and not self.turn:
            self.player2.update()

        if self.board.checkWin():
            self.endScreen: EndScreen = EndScreen("Player 1" if self.turn else "Player 2", self)
        elif self.board.checkTie():
            self.endScreen: EndScreen = EndScreen("tie", self)

        if self.board.checkWin() or self.board.checkTie():
            self.listener.stop()
            self.ended = True


    def run(self) -> None:
        while self.running:
            for event in pg.event.get():
                if event == pg.QUIT:
                    self.running = False

            self.screen.fill(FRAME_COLOUR)
            self.board.draw(self.screen)
            self.update()

            self.leftClick = False
            pg.display.flip()
            self.clock.tick(FPS)