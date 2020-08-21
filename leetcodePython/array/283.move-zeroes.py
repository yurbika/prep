class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == nums.count(0):
            return

        lastZeroIndex = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[lastZeroIndex] = nums[lastZeroIndex], nums[i]
                lastZeroIndex += 1
        # count=nums.count(0)
        # nums[:]=[i for i in nums if i != 0]
        # nums+=[0]*count
