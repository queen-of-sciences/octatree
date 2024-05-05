import io
import sys

import temp2
from PrettyPrint import PrettyPrintTree

"""
Example:

8538183

         3 
     ┌───┴───┐
     8       5 
 ┌───┼───┐   | 
 1   6   2   4 
 |             
 7 
"""

one = temp2.Tree(1)
two = temp2.Tree(2)
three = temp2.Tree(3)
four = temp2.Tree(4)
five = temp2.Tree(5)
six = temp2.Tree(6)
seven = temp2.Tree(7)
eight = temp2.Tree(8)

to_str = PrettyPrintTree(lambda x: x.children, lambda x: x.val, return_instead_of_print=True)

def test_decode(capsys):
    # assert octatree.decode("6165886") == [['6', '1', '3'], ['6', '2'], ['6', '8', '5', '4'], ['6', '8', '7']]  # FixMe :: missing branch
    # assert octatree.decode("8538183") == [['3', '5', '4'], ['3', '8', '1', '7'], ['3', '8', '2'], ['3', '8', '6']]
    # assert octatree.decode("8888888") == [['8', '1'], ['8', '2'], ['8', '3'], ['8', '4'], ['8', '5'], ['8', '6'], ['8', '7']]

    tree = three
    three.add_child(eight)
    eight.add_child(one)
    one.add_child(seven)
    eight.add_child(six)
    eight.add_child(two)
    three.add_child(five)
    five.add_child(four)

    assert to_str(tree) == to_str(temp2.decode("8538183"))

    # FixMe :: automated tests, double check manual first...
    # Note :: 8538183 is good, 6165886 is good, 8888888 is good, 8531183 is good, consider more edge cases and automated test it!
