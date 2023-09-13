import random
import copy


class AI:
    def __init__(self, random_ai=1, player=2):
        self.random_ai = random_ai
        self.player = player

    def random_choice(self, main_game_board):
        empty_squares = main_game_board.get_empty_squares()
        random_move_index = random.randrange(0, len(empty_squares))

        return empty_squares[random_move_index]

    def minimax(self, main_game_board, maximizing):
        case = main_game_board.final_state_of_game() # terminal case
        if case == 1:
            return 1, None

        if case == 2:
            return -1, None

        elif main_game_board.is_full():
            return 0, None

        if maximizing:
            maximal_evaluation = -100
            best_move = None
            empty_squares = main_game_board.get_empty_squares()

            for (row, column) in empty_squares:
                new_board = copy.deepcopy(main_game_board)
                new_board.mark_square(row, column, 1)
                evaluation = self.minimax(new_board, False)[0]
                if evaluation > maximal_evaluation:
                    maximal_evaluation = evaluation
                    best_move = (row, column)
            return maximal_evaluation, best_move

        elif not maximizing:
            minimal_evaluation = 100
            best_move = None
            empty_squares = main_game_board.get_empty_squares()

            for (row, column) in empty_squares:
                new_board = copy.deepcopy(main_game_board)
                new_board.mark_square(row, column, self.player)
                evaluation = self.minimax(new_board, True)[0]
                if evaluation < minimal_evaluation:
                    minimal_evaluation = evaluation
                    best_move = (row, column)
            return minimal_evaluation, best_move

    def evaluate(self, main_game_board):
        if self.random_ai == 0:
            evaluation = 'random'
            move = self.random_choice(main_game_board)
        else:
            # minimax algorithm choice
            evaluation, move = self.minimax(main_game_board, False)

        print(f'AI has chosen to mark the square in pos {move} with an evaluation of: {evaluation}')

        return move