from src.decode import de
from src.util import pretty

"""
    OCTATREES
        - All digits 1 to 8 are arranged in a tree
        - There is a single digit at the root (drawn at the top)
        - Every other digit has another digit as its parent
            s.t when moving up the tree, each non-root digit has a unique path to the root
        -  The order that child nodes are drawn does not matter
            for simplicity they are drawn in increasing order from left to right
        - A leaf is a digit that is not the parent of any other digit
        - The code for an octatree is a sequence of 7 digits and is obtained by:
            Removing the numerically smallest leaf and writing its parent
            Continuing until only the root remains
        
        Example: 8538183 
                 3 
             ┌───┴───┐
             8       5 
         ┌───┼───┐   | 
         1   6   2   4 
         |             
         7 
"""

code = "8538183"

tree = de(code)

pretty(tree)
