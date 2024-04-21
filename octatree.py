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

# Representation on screen

# print root, etc -> e.g
"""
8538183

3
5 8
4 1 2 6
  7
"""


def code(n):
    """ Print the code for a given octatree """
    print(n)


# def decode(string):
#     """ Draw the octatree for a given code of 7 digits"""
#     digits = list(string[::-1])
#     root = digits[0]
#
#     branches = []
#     next_branch = []
#     i = 0
#     while i < len(digits):
#         current = digits[i]
#         if current == root:              # New Branch
#             if len(next_branch) != 0:
#                 branches.append(next_branch)
#                 next_branch = []
#             next_branch.append(root)
#         elif digits[i - 1] == root:      # Child Node
#             next_branch.append(current)
#         elif current < digits[i - 1]:    # Child Node
#             next_branch.append(current)
#         else:                            # Sibling Node
#             next_branch.append("0")
#             branches.append(next_branch)
#             next_branch = [, current]
#         i += 1
#
#     print(branches)

    """
    Identify root: [[3]]
Consider len - 2: this is going to be a child of root therefore [[root, child_1]]
Consider len - 3 (x): if x < child_11, then its a child_1_1, else its a child_2]
Consider len - n (n): if n < (len - n + 1), then its a child, else its a sibling

    Reversing things
    [0] -> root
    [1] is child bc [x - 1] is root
    """


"""
8538183 (FIRST CHILDREN)
[[3, 5, 4], [3, 8, 1, 7], [3, 8, 2], [3, 8, 6]]

- Find each instance of 3 and take the number before it (5, 8)
- if first? -> placeholder with zero?

SECOND CHILDREN, for each first child: w/o 1st and root -> x8(3) x53 x8(3) x183
-

Finding Branches...
Start at root and loop:
len - 1 => root
len - 2 => a first child
len - 3 => either a second child or another first child, decision...

Condition for same branch is that numbers descend from first child...


x8(3) x53 x8(3) x183

LEAVES -> find missing digits and insert into X, ascending...

Identify root: 8538183 -> 853818(3) : len - 1 
Find first children: 8538183 -> 8(5)381(8)3 : (index of root instances) - 1

Steps for building branches:
[[3, 5, 4], [3, 8, 1, 7], [3, 8, 2], [3, 8, 6]]

Identify root: [[3]]
Consider len - 2: this is going to be a child of root therefore [[root, child_1]]
Consider len - 3 (x): if x < child_11, then its a child_1_1, else its a child_2]
Consider len - n (n): if n < (len - n + 1), then its a child, else its a sibling

 



8538183
(0)8[3](0)53(0)8[3](0)183

3818358
81858 [rootless]

Branches of the form [root, ..., leaf]

loop:
    if i == 0: => first child, therefore add to this_branch
    if i != 1: => 
        if i < i - 1, then next child, therefore add to this_branch
        if i > + 1, then must new branch, therefore append LEAF, add branch and set up next_branch
        next_branch = [root]
    


3
5 8
4 1 2 6
  7
"""



def decode(string):
    """ Draw the octatree for a given code of 7 digits"""

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
        if len(rootless) == 1:             # Final Branch
            next_branch.append(current)
            next_branch.append("0")
            branches.append(next_branch)
            del rootless[0]
        elif current == root:                # New Branch
            next_branch.append("0")
            branches.append(next_branch)
            next_branch = [root]
            del rootless[0:i + 1]
            i = 0
        elif i == 0:                       # First Child
            next_branch.append(current)
            i += 1
        elif current < rootless[i - 1]:    # Child Node
            next_branch.append(current)
            i += 1
        elif current > rootless[i - 1]:    # Sibling Node
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

    print(branches)


decode("8538183")
