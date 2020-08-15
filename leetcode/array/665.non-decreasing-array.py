class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True

        index = None

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if index is not None:
                    return False
                else:
                    index = i

        if index is None or index == 0 or index == len(nums)-2 or nums[index-1] <= nums[index+1] or nums[index+2] >= nums[index]:
            return True
        return False
