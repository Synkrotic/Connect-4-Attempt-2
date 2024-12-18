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


    # def lookInFuture(self, playerID: int, board: Board, turns: int) -> tuple[int, int]:
    #     if turns == 0: return self.getBestMove(playerID)

    #     for x in range(self.board.columns):
    #         canAIWin: int = self.canPlayerWin(playerID, board)
    #         canUserWin: int = self.canPlayerWin(self.getOtherUser(playerID), board)

    #         if canAIWin != -1: return (canAIWin, board.getLowestYInColumn(canAIWin))
    #         if canUserWin != -1: return (canUserWin, board.getLowestYInColumn(canUserWin))

            

    #         self.lookInFuture(self.getOtherUser(playerID), boardCopy, turns - 1)


    def getBestMove(self, playerID: int) -> tuple[int, int]:
        """Returns the best move for the AI."""
        scores: list[int] = []
        otherWin: int = self.canPlayerWin(self.getOtherUser(playerID), self.game.board)
        if otherWin != -1: return (otherWin, self.game.board.getLowestYInColumn(otherWin))

        for i in range(self.game.board.columns):
            board: Board = self.game.board.copy()
            coords: tuple[int, int] = (i, board.getLowestYInColumn(i))
            board.setItemAt(playerID, coords)

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
        