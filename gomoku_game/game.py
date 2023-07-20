WINNER_COUNT = 3
EMPTY_CELL = ' - '


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[EMPTY_CELL for col in range(self.size)] for row in range(self.size)]
        self.total_number_of_cells = self.size * self.size

    def check_move(self, i, j) -> bool:
        """
        within board boundaries
        chosen cell is free
        """
        if not 0 <= i < len(self.board) or not 0 <= j < len(self.board[0]):  # outside boundaries
            print('outside boundaries')
            return False
        if self.board[i][j] != EMPTY_CELL:  # cell already in use
            print('already in use')
            return False
        return True

    def update_board(self, i, j, symbol):
        self.board[i][j] = symbol

    def check_winner(self, row, col):
        horizontal = self.horizontal_check(row, col)
        vertical = self.vertical_check(row, col)
        diagonal = self.diagonal_check(row, col)
        return horizontal or vertical or diagonal

    def horizontal_check(self, row, col):
        forward_count = self.is_consecutive_line(row, col, 0, 1)
        back_count = self.is_consecutive_line(row, col, 0, -1)
        if forward_count + 1 + back_count == WINNER_COUNT:
            return True
        return None

    def vertical_check(self, row, col):
        down_count = self.is_consecutive_line(row, col, 1, 0)
        up_count = self.is_consecutive_line(row, col, -1, 0)
        if up_count + 1 + down_count == WINNER_COUNT:
            return True
        return None

    def diagonal_check(self, row, col):
        down_count = self.is_consecutive_line(row, col, -1, 1)
        up_count = self.is_consecutive_line(row, col, 1, -1)
        if up_count + 1 + down_count == WINNER_COUNT:
            return True

        up_count = self.is_consecutive_line(row, col, -1, -1)
        down_count = self.is_consecutive_line(row, col, 1, 1)
        if up_count + 1 + down_count == WINNER_COUNT:
            return True
        return None

    def is_consecutive_line(self, row, col, row_direction, col_direction):
        counter = 0
        for i in range(1, WINNER_COUNT):
            new_row = row + i * row_direction
            new_col = col + i * col_direction
            if not 0 <= new_row < len(self.board) or not 0 <= new_col < len(self.board[new_row]):
                break
            if self.board[new_row][new_col] != self.board[row][col]:
                break
            counter += 1
        return counter

    def clean(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col] = EMPTY_CELL

    def print_board(self):
        for row in self.board:
            row_list = []
            for col in row:
                row_list.append(col)
            print(''.join(row_list))


class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name


class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.player1 = Player(' X ', 'player 1')
        self.player2 = Player(' O ', 'player 2')
        self.number_of_moves = 0

    def get_user_input(self):
        input_string = input()
        try:
            if input_string.lower().strip() == 'restart':
                self.restart()
                print('restarted the game')
                return None
            i, j = input_string.split()
            i, j = int(i), int(j)
            return i, j
        except ValueError as e:
            print(str(e))
            return None

    def execute(self):
        while True:
            if self.number_of_moves == self.board.total_number_of_cells:
                print('draw')
                return
            current_player = self.player1 if self.number_of_moves % 2 == 0 else self.player2
            print(f'{current_player.name} -->{current_player.symbol} enter coordinates.')
            coordinates = self.get_user_input()
            if not coordinates:
                continue
            i, j = coordinates
            is_valid = self.board.check_move(i, j)
            if not is_valid:
                continue
            self.board.update_board(i, j, current_player.symbol)
            self.board.print_board()
            self.number_of_moves += 1
            winner = self.board.check_winner(i, j)
            if not winner:
                continue
            print(f'{current_player.name} won')
            return

    def restart(self):
        self.number_of_moves = 0
        self.board.clean()

    def main(self):
        while True:
            self.execute()
            self.restart()
            print('Play again? (yes/no)')
            again = input()
            if again.lower().strip() == 'no':
                break


if __name__ == '__main__':
    print('Enter board size')
    size = int(input())
    game = Game(size)
    game.main()
