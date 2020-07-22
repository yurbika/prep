class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left  = left
        self.right = right

    def print_tree_inorder(self,tree):
        if tree == None: 
            return
        self.print_tree_inorder(tree.left)
        print(tree.data)
        self.print_tree_inorder(tree.right)

    def print_tree_postorder(self,tree):
        if tree == None: 
            return
        self.print_tree_postorder(tree.left)
        self.print_tree_postorder(tree.right)
        print(tree.data)

    
    def print_tree_preorder(self,tree):
        if tree == None: 
            return
        print(tree.data)
        self.print_tree_preorder(tree.left)
        self.print_tree_preorder(tree.right)

    def __str__(self):
        return str(self.data)

tree = Tree(1, Tree(2,Tree(33),Tree(21)), Tree(3))

print("inorder:")
tree.print_tree_inorder(tree)
print("preorder:")
tree.print_tree_preorder(tree)
print("postorder:")
tree.print_tree_postorder(tree)
