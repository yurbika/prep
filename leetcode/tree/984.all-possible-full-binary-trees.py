# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for i in range(N):
                j = N - 1 - i
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(j):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        ans.append(node)

            Solution.memo[N] = ans

        return Solution.memo[N]


test = Solution()
test.allPossibleFBT(7)
