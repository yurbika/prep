class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                continue
            elif nums[i] + nums[i-1] < nums[i]:
                continue
            else:
                nums[i] = nums[i-1] + nums[i]
        return max(nums)
