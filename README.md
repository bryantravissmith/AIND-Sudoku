# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  

The use of constraint propagation is the same as elimination numbers because they are already selected in the same unit and filling values that have only once choice.  In addition to these two constraints.  With the naked twin constraint, we cycle each unit, and look for sets of cells that have the same two options.  When this condition is met, the these two digits are elimated from the remaining 7 cells in the unit.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  

Constraint propagation is used by setting up 29 unit sets where each of 9 rows are a unit, each of 9 columns are a unit, each of 9 9x9 squares are a unit, and the 2 diagnoal rows are a unit.   From this set of 29 units we can generate a set of peers for each cell.

We for each cell, we can *elimiate* options for the cell by iterating through the peers of the cell.  If the peer has only one value, we can remove that value for the list of options for the cell.

Next, we can reiterate through the 29 units.  For a given unit, we can iterate through the digits 1-9 and find how many cells have that digit as an options.  If a cell is the *only choice* for the digit, we set the value of the cell to that digit.

The next step is to execute on the naked-twin solution to further reduce the  options as stated above.

Constraint propigation has been used to reduce the soduku as much as possible If so, we can return the solved soduku.  If not, then we have to begin to search through the possible options.   

When this happens, we take the best guess of a value for a cell, then seeing if we can solve the soduku for the guessed value.  Constrained Propigation is applied on the guessed soduku.  If no solution is yielded, the another guess is made recursively until a solution or no solution is yielded.  If no-solution is yielded, then we attempt find a solution with the other guess.  Ultimately, we perform depth first search after the constrained propigation is applied to reduce the soduku.  






### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in function.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.