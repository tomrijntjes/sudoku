from solver import Solver,BoxlessSolver,DiagonalSolver


s = Solver()

for sudoku in open('hardest.txt'):
	s.solve(sudoku)

