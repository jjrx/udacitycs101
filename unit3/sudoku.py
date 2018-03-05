# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(square_grid):
  # checks if each row is valid
  # initializes a new list (called row_check)
  # i add every number in the first row to that list
  
    for row in square_grid:
        row_check = []
        for num in row:
            row_check.append(num)
            
  # then i iterate through each number that should be in the list (e.g. 1-3 for a 3x3 grid)
  # and check to see if every number from 1-3 (for example) is in my row_check list
  # if not, this means that the row does not adhere to sudoku guidelines
  
        for i in range(1,len(square_grid)+1):
            if i not in row_check:
                return False
     
  # checks if each column is valid
  # initializes a new column (called col_check)
  # i iterate from 0 to however big square_grid is to access every element in each row
  # EX: for i = 0, i append the 0th term of each row to create a list of elements in the first column
 
    for i in range(0, len(square_grid)):
        col_check = []
        for col in square_grid:
            col_check.append(col[i])

  # then i iterate through each number that should be in the list (e.g. 1-3 for a 3x3 grid)
  # and check to see if every number from 1-3 (for example) is in my col_check list
  # if not, this means that the column does not adhere to sudoku guidelines 
  
        for j in range(1, len(square_grid)+1):
            if j not in col_check:
                return False
            j += 1
        
    return True
       
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
