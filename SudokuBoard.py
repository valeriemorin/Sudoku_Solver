class SudokuBoard:

    def __init__(self):
        self.sudoku_board = []

    # This function takes a csv file of integers representing a game of sudoku
    # This code requires that unknown values are given a value of 0 in the csv
    # This ensures that the script can easily parse file into integer 2D array
    def set_sudoku_board(self, sudoku_board_filepath):

        file = open(sudoku_board_filepath, "r")

        for line in file:
            num_line = []

            for element in line.split(','):
                num_line.append(int(element.strip('\n')))

            self.sudoku_board.append(num_line)

        file.close()

    # The getter function for the sudoku board 2D array
    def get_sudoku_board(self):
        return self.sudoku_board

    # This prints the current sudoku board into the console
    def print_sudoku_board(self):

        row_count = 0

        for row in self.sudoku_board:
            col_count = 0
            linestring = "|  "

            for col in row:
                if col == 0:
                    linestring += "# "
                else:
                    linestring += "%d " % col
                col_count += 1

                if col_count % 3 == 0:
                    linestring += " |  "

            if row_count % 3 == 0:
                print("-------------------------------")

            print(linestring)

            row_count += 1

        print("-------------------------------")

    # This function updates a specific position on the sudoku board with a specific value
    def update_sudoku_board(self, row, col, value):
        self.sudoku_board[row][col] = value

