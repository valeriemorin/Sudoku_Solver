# There are 9 sections in a sudoku puzzle which requires
def get_section_coords(row, col):
    if row in [0, 1, 2] and col in [0, 1, 2]:  # Section 1
        return [0, 1, 2], [0, 1, 2]
    elif row in [0, 1, 2] and col in [3, 4, 5]:  # Section 2
        return [0, 1, 2], [3, 4, 5]
    elif row in [0, 1, 2] and col in [6, 7, 8]:  # Section 3
        return [0, 1, 2], [6, 7, 8]
    elif row in [3, 4, 5] and col in [0, 1, 2]:  # Section 4
        return [3, 4, 5], [0, 1, 2]
    elif row in [3, 4, 5] and col in [3, 4, 5]:  # Section 5
        return [3, 4, 5], [3, 4, 5]
    elif row in [3, 4, 5] and col in [6, 7, 8]:  # Section 6
        return [3, 4, 5], [6, 7, 8]
    elif row in [6, 7, 8] and col in [0, 1, 2]:  # Section 7
        return [6, 7, 8], [0, 1, 2]
    elif row in [6, 7, 8] and col in [3, 4, 5]:  # Section 8
        return [6, 7, 8], [3, 4, 5]
    elif row in [6, 7, 8] and col in [6, 7, 8]:  # Section 9
        return [6, 7, 8], [6, 7, 8]


class SudokuSolver:

    sb = None
    gd = {}

    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.sb = self.sudoku_board.get_sudoku_board()
        self.gd = {}

    def fill_guess_dictionary(self):
        for i in range(len(self.sb)):
            for j in range(len(self.sb[i])):
                if self.sb[i][j] == 0:
                    self.gd[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                else:
                    continue

    def elim_from_row(self, row, col):
        for num in self.sb[row]:
            if num != 0 and num in self.gd[row, col]:
                self.gd[(row, col)].remove(num)

    def elim_from_col(self, row, col):
        for i in range(len(self.sb)):
            for j in range(len(self.sb[i])):
                if j == col and self.sb[i][j] != 0 and self.sb[i][j] in self.gd[row, col]:
                    self.gd[(row, col)].remove(self.sb[i][j])

    def elim_from_section(self, row, col):
        section_coords = get_section_coords(row, col)
        for i in section_coords[0]:
            for j in section_coords[1]:
                if self.sb[i][j] != 0 and self.sb[i][j] in self.gd[row, col]:
                    self.gd[(row, col)].remove(self.sb[i][j])

    def solve_sudoku_board(self):
        # get possible numbers for each position with value 0
        # need to check row, col, and section
        # dictionary{tuple(row, col), list[possible values]}
        self.fill_guess_dictionary()

        iter_count = 0
        # While Dictionary.length > 0
        while len(self.gd.items()) > 0:

            iter_count += 1

            for key in self.gd.keys():
                # Check row for numbers to delete
                # Check col for numbers to delete
                # Check section for numbers to delete
                self.elim_from_row(key[0], key[1])
                self.elim_from_col(key[0], key[1])
                self.elim_from_section(key[0], key[1])

            # if any dictionaries only have one guess,
            #       plot value on board
            #       delete item from dict

            for item in list(self.gd.items()):
                if len(item[1]) == 1:
                    self.sudoku_board.update_sudoku_board(item[0][0], item[0][1], item[1][0])
                    del self.gd[item[0]]

            print("\n@@@@@@@@@ Iteration %3d @@@@@@@@@" % iter_count)
            self.sudoku_board.print_sudoku_board()

