# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _countNodes(self, root, cnt):
        if not root:
            return cnt

        if root.left:
            cnt += 1
            cnt = self._countNodes(root.left, cnt)
        if root.right:
            cnt += 1
            cnt = self._countNodes(root.right, cnt)

        return cnt

    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        if root:
            return self._countNodes(root, cnt)+1
        else:
            return cnt
