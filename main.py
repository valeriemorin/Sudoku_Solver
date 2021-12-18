# Single Candidate Sudoku Solver
# Script developed by Valerie Morin on December 16, 2021

import SudokuBoard
import SudokuSolver


def main():

    # Creating the sudoku board
    sb = SudokuBoard.SudokuBoard()
    sb.set_sudoku_board("SudokuPuzzle.txt")
    sb.print_sudoku_board()

    # Solving the sudoku puzzle
    ss = SudokuSolver.SudokuSolver(sb)
    ss.solve_sudoku_board()


main()
