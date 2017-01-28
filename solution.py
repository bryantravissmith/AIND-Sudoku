assignments = []
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
unitlist = ([cross(rows,c) for c in cols]+\
[cross(r,cols) for r in rows]+\
[cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])+\
[["".join(t) for t in zip(rows,digits)]]+\
[["".join(t) for t in zip(reversed(rows),digits)]]

squares = cross(rows,cols)
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    inverse_values = dict()
    for k, v in values.items():
        if(len(v)==2):
            inverse_values[v] = inverse_values.get(v, [])
            inverse_values[v].append(k)

    # Eliminate the naked twins as possibilities for their peers
    for unit in unitlist:
        for twin, cells in inverse_values.items():
        	# Counts the number of cells witht he twin values in each unit
            if sum([1 for cell in cells if cell in unit]) == 2:
                for cell in unit:
                	# If cell is not a twin, remove the twin digits
                    if cell not in cells:
                        for digit in twin:
                            values[cell] = values[cell].replace(digit,"")
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = dict(zip(cross(rows,cols),grid))
    for cell in values:
        if values[cell] == '.':
            values[cell] = '123456789'
    return values

def display(values):
    """
    Display the values as a 2-D grid in stdout from Norvig's Blog
    Args:
        values(dict): The sudoku in dictionary form
    """
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print("".join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()

def eliminate(values):
    """
    Elimiates options for cells if that options is a value in a peer cell
    Args:
        values(dict): The sudoku in dictionary form
    """
    vals = values.copy()
    for cell in values:
        if len(values[cell]) > 1:
            for peer in peers[cell]:
                if len(values[peer]) == 1:
                    vals[cell] = vals[cell].replace(values[peer],"")
    return vals

def only_choice(values):
    """
    Sets a cell value to a digit if that cell is the only options for 
    that digit
    Args:
        values(dict): The sudoku in dictionary form
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    """
    Applies constrained propigation to the sudoku while it contiues to 
    elimation options from cells through the application of elimation, 
    only choice, and nake_twin.
    Args:
        values(dict): The sudoku in dictionary form
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)
        # Add Naked twi
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def solve(grid):
    """
    Converst a string representation of a sudou to a dictionary and solves
    that soduku returning the solved sudoku in a dictionary form.
    Args:
        grid(string): The sudoku in dictionary form
    """
    values = search(grid_values(grid))
    #display(values)
    return values

def search(values):
    """
    Recursive function for redusing and searching through all possible 
    solutions to find the/a solution to the soduku
    Args:
        values(dict): The sudoku in dictionary form
    """
    if values is None:
        return None
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    
    if values:
        if sum([len(v) for v in list(values.values())])==81:
            return values
        
    # Chose one of the unfilled square s with the fewest possibilities
        min_len = min([len(a) for a in list(values.values()) if len(a) != 1])
        final_cell = None
        for cell in values:
            if len(values[cell])==min_len:
                final_cell = cell
                break
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
        for val in values[final_cell]:
            vals = values.copy()
            vals[final_cell] = val
            vals = search(vals)
            if vals is not None:
                return vals
    
    return None

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid_values(diag_sudoku_grid))
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
