from PrettyPrint import PrettyPrintTree


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

to_str = PrettyPrintTree(lambda x: x.children, lambda x: x.val, return_instead_of_print=True)
