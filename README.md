# SudokuSolver
A sudoku solver written in python

Simply place an unsolved sudoku in sudoku.txt with column values separated by spaces and row values separated by newlines. Any unsolved values must be represented by 0.

This does not employ any advanced techniques. It simply uses the box and row rules for sudoku and recursive backtracking. As such, it can be somewhat slow.

The initial grid must not violate any sudoku rules. If there is a duplicate value in a row or box in the initial grid then the program might not catch it.
