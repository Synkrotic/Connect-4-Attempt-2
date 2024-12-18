import threading, pygame as pg
from game import Game
from data import *
from pynput import mouse

pg.init()
pg.font.init()

while True:
    game: Game = Game(ai=True)
    game.run()