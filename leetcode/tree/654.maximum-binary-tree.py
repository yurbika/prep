# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTree(self, arr, root):
        if not arr:
            return None

        if len(arr) == 1:
            return TreeNode(arr[0])

        if arr[:arr.index(max(arr))]:
            root.left = self.createTree(
                arr[:arr.index(max(arr))], TreeNode(max(arr[:arr.index(max(arr))])))
        if arr[arr.index(max(arr))+1:]:
            root.right = self.createTree(
                arr[arr.index(max(arr))+1:], TreeNode(max(arr[arr.index(max(arr))+1:])))

        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = TreeNode(max(nums))
        self.createTree(nums, root)
        print(root)
        return root
