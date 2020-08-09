class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    result += [[nums[i], nums[j], nums[k]]]
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                if nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return result
