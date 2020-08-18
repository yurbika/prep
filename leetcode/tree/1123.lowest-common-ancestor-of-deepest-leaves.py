# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lca(self, root):
        if not root:
            return 0, None
        h1, lca1 = self.lca(root.left)
        h2, lca2 = self.lca(root.right)
        # comes from left
        if h1 > h2:
            return h1 + 1, lca1
        # comes from right
        if h1 < h2:
            return h2 + 1, lca2
        # root self is lca
        return h1 + 1, root

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.lca(root)[1]
