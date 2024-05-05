from src.util import nodes


def de(code):
    """ Find the octatree for a given code of 7 digits """
    # 1. Reverse string
    digits = list(code[::-1])

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

    return tree
