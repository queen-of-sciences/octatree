import octatree

"""
Example:

8538183

3
5 8
4 1 2 6
  7
"""


def test_decode():
    assert octatree.decode("6165886") == [['6', '1', '3'], ['6', '2'], ['6', '8', '5', '4'], ['6', '8', '7']]  # FixMe :: missing branch
    assert octatree.decode("8538183") == [['3', '5', '4'], ['3', '8', '1', '7'], ['3', '8', '2'], ['3', '8', '6']]
    assert octatree.decode("8888888") == [['8', '1'], ['8', '2'], ['8', '3'], ['8', '4'], ['8', '5'], ['8', '6'], ['8', '7']]
