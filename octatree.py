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


def code(n):
    """ Print the code for a given octatree """
    # TODO


def decode(string):
    """ Draw the octatree for a given code of 7 digits"""
    print(f"\nDecoding [{string}]")

    # 1. Reverse string
    digits = list(string[::-1])

    # 2. Remove the initial instance of root
    root = digits[0]
    rootless = digits[1:]

    # 3. Construct branches
    i = 0
    branches = []
    next_branch = [root]
    while len(rootless) > 0:
        current = rootless[i]
        if len(rootless) == 1:  # Final Branch
            if current == root:
                next_branch.append("0")
                branches.append(next_branch)
                next_branch = []
            next_branch.append(current)
            next_branch.append("0")
            del rootless[0]
            branches.append(next_branch)
        elif current == root:  # New Branch
            next_branch.append("0")
            branches.append(next_branch)
            next_branch = [root]
            del rootless[0:i + 1]
            i = 0
        elif i == 0:  # First Child
            next_branch.append(current)
            i += 1
        elif current < rootless[i - 1]:  # Child Node
            next_branch.append(current)
            i += 1
        elif current >= rootless[i - 1]:  # Sibling Node
            next_branch.append("0")
            branches.append(next_branch)
            next_branch = [root]
            del rootless[0:i]
            i = 0

    # 4. Find Leaves
    leaves = []
    i = 1
    while i <= 8:
        if str(i) not in digits:
            leaves.append(i)
        i += 1

    print(leaves)

    # 5. Insert Leaves
    leaves.reverse()
    for i in range(len(branches)):
        for j in range(len(branches[i])):
            if branches[i][j] == '0':
                branches[i][j] = str(leaves.pop(0))

    branches.sort()
    print(branches)
    return branches


decode("8538183")
# 6165886 -> # FixMe :: missing branch
# 8888888
