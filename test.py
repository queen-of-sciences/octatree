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

one = decode.Tree(1)
two = decode.Tree(2)
three = decode.Tree(3)
four = decode.Tree(4)
five = decode.Tree(5)
six = decode.Tree(6)
seven = decode.Tree(7)
eight = decode.Tree(8)

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

    assert to_str(tree) == to_str(decode.decode("8538183"))

    # FixMe :: automated tests, double check manual first...
    # Note :: 8538183 is good, 6165886 is good, 8888888 is good, 8531183 is good, consider more edge cases and automated test it!
