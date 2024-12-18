import pygame as pg
from rectangle import Rectangle
from data import *

class Board:
    def __init__(self, rows: int, columns: int):
        self.rows: int = rows
        self.columns: int = columns
        self.layout: list[list[int]] = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.feetRect: Rectangle = Rectangle(SCREEN_WIDTH - FRAME_FEET_WIDTH * 2, FRAME_FEET_HEIGHT * 2, FRAME_FEET_WIDTH, SCREEN_HEIGHT - FRAME_FEET_WIDTH, BACKGROUND_COLOUR, DEFAULT_BORDER_RADIUS)
    

    def getInverseCoords(self, x: int, y: int) -> tuple:
        return (x, self.rows - y - 1)


    def setItemAt(self, player: int, coords: tuple[int, int]) -> None:
        if player < 0 or player > 2:
            print(f"\033[91m{ERROR_INVALID_PLAYERID}\033[0m")
            return
        if coords[0] < 0 or coords[0] > self.rows or coords[1] < 0 or coords[1] > self.columns:
            print(f"\033[91m{ERROR_INVALID_COORDS}\033[0m")
            return
        
        
        self.layout[coords[1]][coords[0]] = player


    def getItemAt(self, coords: tuple[int, int]) -> int:
        if coords[0] < 0 or coords[0] > self.rows or coords[1] < 0 or coords[1] > self.columns:
            print(f"\033[91m{ERROR_INVALID_COORDS}\033[0m")
            return -1
        
        return self.layout[coords[0]][coords[1]]
    

    def getLowestYInColumn(self, x: int) -> int:
        for y in range(self.rows - 1, -1, -1):
            if self.layout[y][x] == 0:
                return y
        print(f"\033[91m{ERROR_COLUMN_FULL}\033[0m")
        return -1
    

    def showInTerminal(self) -> None:
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.layout[row][column], end=" | ")
            print("\n" + ("-" * self.columns * 4))
    

    def copy(self) -> 'Board':
        board: Board = Board(self.rows, self.columns)
        board.layout = [row[:] for row in self.layout]
        return board


    def draw(self, screen: pg.display) -> None:
        self.feetRect.draw(screen)
        for i in range(self.rows):
            for j in range(self.columns):
                
                colour: tuple[int, int, int]
                x: int = columnBoundaries[j][0] + CIRCLE_DIAMETER // 2
                y: int = SCREEN_HEIGHT - (FRAME_FEET_HEIGHT * 2 + FRAME_MARGIN) - ((CIRCLE_DIAMETER + CIRCLE_PADDING) * (self.rows - i - 1))
                
                if self.layout[i][j] == 1: colour = player1Colour
                elif self.layout[i][j] == 2: colour = player2Colour
                else: colour = BACKGROUND_COLOUR

                pg.draw.circle(screen, colour, (x, y), CIRCLE_DIAMETER // 2)




    def checkTie(self) -> bool:
        for i in range(self.rows):
            for j in range(self.columns):
                if self.layout[i][j] == 0: return False
        return True
    

    def checkWin(self) -> bool:
        for i in range(self.rows):
            for j in range(self.columns):
                if self.layout[i][j] == 0: continue
                if (self.checkHorizontal(i, j) == WINSCORE) or (
                    self.checkVertical(i, j) >= WINSCORE) or (
                    self.checkDiagonalLeft(i, j) >= WINSCORE) or (
                    self.checkDiagonalRight(i, j) >= WINSCORE): return True
        return False
    

    def checkHorizontal(self, x: int, y: int) -> int:
        player: int = self.layout[x][y]
        if player == 0: return 0
        for i in range(4):
            if y + i >= self.columns: return -1
            if self.layout[x][y + i] != player: return i
        return WINSCORE
    

    def checkVertical(self, x: int, y: int) -> int:
        player: int = self.layout[x][y]
        if player == 0: return 0
        for i in range(4):
            if x + i >= self.rows: return -1
            if self.layout[x + i][y] != player: return i
        return WINSCORE


    def checkDiagonalLeft(self, x: int, y: int) -> int:
        player: int = self.layout[x][y]
        if player == 0: return 0
        for i in range(4):
            if x + i >= self.rows or y + i >= self.columns: return -1
            if self.layout[x + i][y + i] != player: return i
        return WINSCORE
    

    def checkDiagonalRight(self, x: int, y: int) -> int:
        player: int = self.layout[x][y]
        if player == 0: return 0
        for i in range(4):
            if x + i >= self.rows or y - i < 0: return -1
            if self.layout[x + i][y - i] != player: return i
        return WINSCORE
    

    def getBoardScore(self) -> int:
        score: int = 0
        for i in range(self.rows):
            for j in range(self.columns):
                score += self.checkHorizontal(i, j)
                score += self.checkVertical(i, j)
                score += self.checkDiagonalLeft(i, j)
                score += self.checkDiagonalRight(i, j)
        return score