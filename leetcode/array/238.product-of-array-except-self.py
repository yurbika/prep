import functools


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = functools.reduce(lambda i, j: i*j, nums)
        if product == 0 and nums.count(0) > 1:
            return [0]*len(nums)

        elif product == 0 and nums.count(0) == 1:
            temp = []
            temp = nums[:nums.index(0)]+nums[nums.index(0)+1:]
            product = functools.reduce(lambda i, j: i*j, temp)
            index = nums.index(0)
            nums = [0 for i in range(len(nums))]
            nums[index] = product

        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = round(product/nums[i])
        return nums
