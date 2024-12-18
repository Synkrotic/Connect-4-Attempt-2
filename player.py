import pygame as pg
from data import *

class Player():
    def __init__(self, game: 'Game', id: int): # type: ignore
        self.game: 'Game' = game # type: ignore
        self.ID: int = id


    def update(self) -> None:
        xCoord: int = pg.mouse.get_pos()[0]
        column: int = self.getColumn(xCoord)

        yCoord: int = self.game.board.getLowestYInColumn(column)
        if yCoord == -1: return
        self.game.board.setItemAt(self.ID, (column, yCoord))
        self.game.turn = not self.game.turn

    
    def getColumn(self, xCoord: int) -> int:
        """Returns the column number which is calculated by the x coordinate of the mouse.
            If you aren't hovering over a column, it returns -1."""
        for column, boundaries in columnBoundaries.items():
            if (boundaries[0] <= xCoord <= boundaries[1]): return column
        return -1