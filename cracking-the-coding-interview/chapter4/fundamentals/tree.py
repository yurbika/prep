class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left  = left
        self.right = right

    def print_tree(self,side,tree):
        if tree == None: 
            return
        print(side,tree.data),
        self.print_tree("left: ",tree.left)
        self.print_tree("right: ",tree.right)

    def __str__(self):
        return str(self.data)

tree = Tree(1, Tree(2,Tree(33),Tree(21)), Tree(3))

tree.print_tree("root: ",tree)