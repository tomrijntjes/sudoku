# sudoku

Usage:

1.install python3
2.install requirements from requirements.txt
3.go to commandline
4.python3 run.py 6000

#method

I generated 10k puzzles by running norvig.py based on his work hosted here http://norvig.com/sudoku.html. Then I attempted every sudoku with DiagonalSolver in solver.py and filtered unsatisfiable puzzles, resulting in diagonal.txt. Finally I ran run.py to test performance of each solver object.

#results
Execute run.py to find that the diagonalsolver is slightly less performant.
