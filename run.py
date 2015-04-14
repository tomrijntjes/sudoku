from solver import Solver,BoxlessSolver,DiagonalSolver


s = Solver()

print('hardest')
for sudoku in open('hardest.txt'):
	print(sudoku)
	print(s.display(s.solve(sudoku)))
