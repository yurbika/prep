# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getChildren(self, root, result):
        if root.left:
            result.append(root.left)
        if root.right:
            result.append(root.right)

    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [root]
        solution = [root.val]
        while stack:
            temp = []
            while stack:
                self.getChildren(stack.pop(0), temp)
            cnt = 0
            for i in temp:
                cnt += i.val
            solution.append(cnt)
            stack += temp

        return solution.index(max(solution))+1
