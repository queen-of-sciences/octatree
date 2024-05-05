from prettyprint import PrettyPrintTree

"""
    Octatrees
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
"""


class Tree:
    def __init__(self, value):
        self.val = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return child


nodes = {
    '1': Tree(1),
    '2': Tree(2),
    '3': Tree(3),
    '4': Tree(4),
    '5': Tree(5),
    '6': Tree(6),
    '7': Tree(7),
    '8': Tree(8)
}

pretty = PrettyPrintTree(lambda x: x.children, lambda x: x.val)


def decode(string):
    """ Draw the octatree for a given code of 7 digits"""
    # 1. Reverse string
    digits = list(string[::-1])

    # 2. Obtain root
    root = digits[0]

    # 3. Obtain leaves
    leaves = []
    i = 1
    while i <= 8:
        if str(i) not in digits:
            leaves.append(str(i))
        i += 1

    # 4. Construct tree
    tree = nodes[root]
    active = None
    prev_active = None
    for i in range(7):
        this = digits[i]
        prev = digits[i - 1] if i > 0 else None

        if this == root:
            if active is not None:
                active.add_child(nodes[leaves.pop()])
            active = tree

        elif prev == root:
            active.add_child(nodes[this])
            active = nodes[this]

        elif this < prev:
            active.add_child(nodes[this])
            active = nodes[this]

        elif this >= prev:
            prev_active.add_child(nodes[leaves.pop()])
            active = nodes[this]

        if i == 6:
            active.add_child(nodes[leaves.pop()])

        i += 1
        prev_active = active

    pretty(tree)
    return tree


def code(n):
    """ Print the code for a given octatree """
    # TODO


decode("8531183")

code(None)
