# Definition for a binary tree node.
class TreeNode:
         def __init__(self, val=0, left=None, right=None):
                    self.val = val
                    self.left = left
                    self.right = right
class Solution:
    def delNodes(self, root: TreeNode, delete: List[int]) -> List[TreeNode]:
        delete = set(delete)
        result = []
        def _delNodes(root,parent):
            if not root:
                return

            if root.val in delete:
                _delNodes(root.left,False)
                _delNodes(root.right,False)
                return
            else:
                if not parent:
                    result.append(root)
                root.left = _delNodes(root.left,True)
                root.right = _delNodes(root.right,True)
                return root
        _delNodes(root,False)
        return result
            