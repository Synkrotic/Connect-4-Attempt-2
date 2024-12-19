import random
import pygame as pg
from data import *
from board import Board

class AIPlayer:
    def __init__(self, game: 'Game', id: int): # type: ignore
        self.game: 'Game' = game # type: ignore
        self.ID: int = id


    def update(self) -> None:
        coords: tuple[int, int] = self.getBestMove(self.ID)
        # self.lookInFuture(self.ID, self.game.board, 1)

        self.game.board.setItemAt(self.ID, coords)
        self.game.turn = not self.game.turn


    def checkIfAllSame(self, scores: list[int]) -> bool:
        """Returns True if all the elements in the list are the same."""
        return all(score == scores[0] for score in scores)


    def getOtherUser(self, playerID: int) -> int:
        """Returns the other user ID."""
        return 1 if playerID == 2 else 2

    
    def canPlayerWin(self, playerID: int, board: Board) -> int:
        """Returns True if the other player can win."""
        for i in range(board.columns):
            boardCopy: Board = board.copy()
            coords: tuple[int, int] = (i, boardCopy.getLowestYInColumn(i))
            boardCopy.setItemAt(playerID, coords)
            if boardCopy.checkWin(): return i
        return -1


    def lookInFuture(self, playerID: int, board: Board, depth: int) -> tuple[int, int]:
        if depth == 0: return self.getBestMove(playerID)

        aiBestMove: tuple[int, int] = self.getBestMove(playerID, board)

        

    def getMoveScore(self, playerID: int, x: int, board: Board) -> int:
        boardScore: int = board.getBoardScore()

        boardCopy: Board = board.copy()
        boardCopy.setItemAt(playerID, (x, boardCopy.getLowestYInColumn(x)))
        boardCopyScore: int = boardCopy.getBoardScore()

        return boardCopyScore - boardScore


    def getBestMove(self, playerID: int, board: Board) -> tuple[int, int]:
        """Returns the best move for the AI."""
        scores: list[int] = []
        otherWin: int = self.canPlayerWin(self.getOtherUser(playerID), self.game.board)
        if otherWin != -1: return (otherWin, self.game.board.getLowestYInColumn(otherWin))

        for i in range(self.game.board.columns):
            board: Board = self.game.board.copy()
            coords: tuple[int, int] = (i, board.getLowestYInColumn(i))
            board.setItemAt(playerID, coords)
            board.draw(self.game.screen)
            pg.image.save(self.game.screen, f"board{i}.png")

            if board.checkWin(): return coords
            
            impact: int = board.getBoardScore() - self.game.board.getBoardScore()
            scores.append(impact)
        
        coords: tuple[int, int]
        if not self.checkIfAllSame(scores):
            highestScoreIndex: int = scores.index(max(scores))
            coords = (highestScoreIndex, self.game.board.getLowestYInColumn(highestScoreIndex))
        else:
            xCoord: int = random.randint(0, self.game.board.columns)
            coords = (xCoord, self.game.board.getLowestYInColumn(xCoord))
        return coords
        