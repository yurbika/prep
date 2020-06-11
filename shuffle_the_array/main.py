class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            print(i,j)
            res += [i,j]
        return res