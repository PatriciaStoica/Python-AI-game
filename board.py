from constants import *
import numpy as np
import pygame
screen = pygame.display.set_mode((width, height))

class Board:
    def __init__(self):
        self.squares = np.zeros((rows, columns))
        self.empty_squares = self.squares  # [squares]
        self.marked_squares = 0

    def final_state_of_game(self, show=False):
        # return 0 if there is no win yet
        # return 1 if player 1 wins
        # return 2 if player 2 wins

        # vertical wins
        for column in range(columns):
            if self.squares[0][column] == self.squares[1][column] == self.squares[2][column] != 0:
                if show:
                    color = circle_color if self.squares[0][column] == 2 else cross_color
                    initial_position = (column * square_size + square_size // 2, 20)
                    final_position = (column * square_size + square_size // 2, height - 20)
                    pygame.draw.line(screen, color, initial_position, final_position, line_width)
                return self.squares[0][column]

        # horizontal wins
        for row in range(rows):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = circle_color if self.squares[row][0] == 2 else cross_color
                    initial_position = (20, row * square_size + square_size // 2)
                    final_position = (width - 20, row * square_size + square_size // 2)
                    pygame.draw.line(screen, color, initial_position, final_position, line_width)
                return self.squares[row][0]

        # desc diagonal win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = circle_color if self.squares[1][1] == 2 else cross_color
                initial_position = (20, 20)
                final_position = (width - 20, height - 20)
                pygame.draw.line(screen, color, initial_position, final_position, cross_width)
            return self.squares[1][1]

        # ascending diagonal win
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = circle_color if self.squares[1][1] == 2 else cross_color
                initial_position = (20, height - 20)
                final_position = (width - 20, 20)
                pygame.draw.line(screen, color, initial_position, final_position, cross_width)
            return self.squares[1][1]

        # no win yet
        return 0

    def mark_square(self, row, column, player):
        self.squares[row][column] = player
        self.marked_squares += 1

    def empty_square(self, row, column):
        return self.squares[row][column] == 0

    def get_empty_squares(self):
        empty_squares = []
        for row in range(rows):
            for column in range(columns):
                if self.empty_square(row, column):
                    empty_squares.append((row, column))
        return empty_squares

    def is_full(self):
        return self.marked_squares == 9

    def is_empty(self):
        return self.marked_squares == 0