import pygame
from constants import *
from game import Game
from ui import UI

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TIC TAC TOE GAME')
screen.fill(background_color)

game = Game()
board = game.console_board
ai = game.ai
ui = UI(game, board, ai)
ui.menu()