class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return
        if len(nums) == 1:
            return nums

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(nums[i])
            else:
                result.append(sum(nums[:i+1]))

        return result
