from PrettyPrint import PrettyPrintTree


class Tree:
    def __init__(self, value):
        self.val = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return child


pt = PrettyPrintTree(lambda x: x.children, lambda x: x.val)
# tree = Tree(3)
# child1 = tree.add_child(Tree(8))
# child2 = tree.add_child(Tree(5))
# child1.add_child(Tree(1))
# child1.add_child(Tree(2))
# child1.add_child(Tree(6))
# child2.add_child(Tree(4))
# pt(tree)


one = Tree(1)
two = Tree(2)
three = Tree(3)
four = Tree(4)
five = Tree(5)
six = Tree(6)
seven = Tree(7)
eight = Tree(8)

nodes = {'1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight}

# tree = three
# three.add_child(eight)
# eight.add_child(one)
# one.add_child(seven)
# eight.add_child(six)
# eight.add_child(two)
# three.add_child(five)
# five.add_child(four)
# pt(tree)


def decode(string):
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
    pretty = PrettyPrintTree(lambda x: x.children, lambda x: x.val)
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

        # Question :: this == prev?

        if i == 6:
            active.add_child(nodes[leaves.pop()])

        i += 1
        prev_active = active

    pretty(tree)
    # return tree


decode("8531183")
