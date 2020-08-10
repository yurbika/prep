class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        while k != 1:
            nums.pop(nums.index(max(nums)))
            k -= 1
        return max(nums)
