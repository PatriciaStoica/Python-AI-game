import pygame
import sys
from constants import *


class UI():

    def __init__(self, game, board, ai):
        self.ai = ai
        self.game = game
        self.board = board

    def menu(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.game.reset()
                        board = self.game.console_board
                        ai = self.ai

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    row = position[1] // square_size
                    column = position[0] // square_size

                    if self.board.empty_square(row, column) and self.game.running:
                        self.game.make_move(row, column)

                        if self.game.isover():
                            self.game.running = False

            if self.game.game_mode == 'ai' and self.game.player_to_mark_square == self.ai.player and self.game.running:
                pygame.display.update()

                row, column = self.ai.evaluate(self.board)
                self.game.make_move(row, column)

                if self.game.isover():
                    self.game.running = False

            pygame.display.update()