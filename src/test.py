from src.decode import de
from src.util import to_str, Tree


def test_decode_8538183():
    code = "8538183"

    one = Tree(1)
    two = Tree(2)
    three = Tree(3)
    four = Tree(4)
    five = Tree(5)
    six = Tree(6)
    seven = Tree(7)
    eight = Tree(8)

    tree = three
    three.add_child(eight)
    eight.add_child(one)
    one.add_child(seven)
    eight.add_child(six)
    eight.add_child(two)
    three.add_child(five)
    five.add_child(four)

    assert to_str(de(code)) == to_str(tree)


def test_decode_6165886():
    code = "6165886"

    one = Tree(1)
    two = Tree(2)
    three = Tree(3)
    four = Tree(4)
    five = Tree(5)
    six = Tree(6)
    seven = Tree(7)
    eight = Tree(8)

    tree = six
    six.add_child(eight)
    eight.add_child(seven)
    eight.add_child(five)
    five.add_child(four)
    six.add_child(one)
    one.add_child(three)
    six.add_child(two)

    assert to_str(de(code)) == to_str(tree)


# "8888888" is also good
# "8531183" too!
