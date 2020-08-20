# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNodes(self, root, result):
        if not root:
            result.append(None)
            return result

        result.append(root.val)
        result = self.getNodes(root.left, result)
        result = self.getNodes(root.right, result)

        return result

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        q = self.getNodes(q, [])
        p = self.getNodes(p, [])

        for i in range(len(q)):
            if q[i] != p[i]:
                return False

        return True
