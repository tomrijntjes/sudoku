from solver import Solver,DiagonalSolver
from scipy.stats import ttest_ind
from numpy import std,mean


s = Solver()
d = DiagonalSolver()

"""
for puzzle in open('random.txt'):
	d.display(puzzle)
	d.display(s.solve(puzzle))
"""


#normal = [d.solve(x) for x in open('random.txt')]

#print("Normal sudoku. Mean: {0} Standard deviation: {1}".format(mean(normal),std(normal)))

"""
hard = [s.solve(x) for x in open('hardest.txt')]
normal = [s.solve(x) for x in open('top95.txt')]
print("Hard sudoku. Mean: {0} Standard deviation: {1}".format(mean(hard),std(hard)))
print("Normal sudoku. Mean: {0} Standard deviation: {1}".format(mean(normal),std(normal)))
two_sample = ttest_ind(normal, hard)

print("The t-statistic is %.3f and the p-value is %.3f." % two_sample)
"""
