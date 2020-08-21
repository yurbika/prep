# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root,l,r,s):
        if not root:
            return s
        
        if root.val >= l and root.val <= r:
            s += root.val
        s = self.traverse(root.left,l,r,s)
        s = self.traverse(root.right,l,r,s)
            
        return s
    
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        s = 0
        if L > R:
            L,R = R,L
            
        return self.traverse(root,L,R,s)