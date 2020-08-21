class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxValue = 0

        for i in range(len(nums)):
            if maxValue < i:
                return False
            if maxValue >= len(nums)-1:
                return True
            maxValue = max(maxValue, i + nums[i])
        return True
