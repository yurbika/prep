class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i < 0:
            return

        if i == 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while nums[j] <= nums[i-1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return
