from board import Board
from ai import AI
import pygame
from constants import *
screen = pygame.display.set_mode((width, height))

class Game:
    def __init__(self):
        self.console_board = Board()
        self.show_lines()
        self.ai = AI()
        self.game_mode = 'ai'
        self.running = True
        self.player_to_mark_square = 1  # 1 - cross, 2 - circles

    def make_move(self, row, column):
        self.console_board.mark_square(row, column, self.player_to_mark_square)
        self.draw_figure(row, column)
        self.next_player()

    def show_lines(self):
        screen.fill(background_color)
        pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height), line_width)
        pygame.draw.line(screen, line_color, (width - square_size, 0), (width - square_size, height), line_width)

        pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
        pygame.draw.line(screen, line_color, (0, height - square_size), (width, height - square_size), line_width)

    def next_player(self):
        self.player_to_mark_square = self.player_to_mark_square % 2 + 1

    def draw_figure(self, row, column):
        if self.player_to_mark_square == 1:
            start_descending_line = (column * square_size + offset, row * square_size + offset)
            end_descending_line = (
                column * square_size + square_size - offset, row * square_size + square_size - offset)
            pygame.draw.line(screen, cross_color, start_descending_line, end_descending_line, cross_width)

            start_ascending_line = (column * square_size + offset, row * square_size + square_size - offset)
            end_ascending_line = (column * square_size + square_size - offset, row * square_size + offset)
            pygame.draw.line(screen, cross_color, start_ascending_line, end_ascending_line, cross_width)
        elif self.player_to_mark_square == 2:
            center = (column * square_size + square_size // 2, row * square_size + square_size // 2)
            pygame.draw.circle(screen, circle_color, center, radius, circle_width)

    def reset(self):
        self.__init__()

    def isover(self):
        return self.console_board.final_state_of_game(show=True) != 0 or self.console_board.is_full()