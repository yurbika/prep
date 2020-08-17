class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) % 2 != 0:
            return

        solution = []

        for i in range(1, len(nums), 2):
            solution += [nums[i]] * nums[i-1]

        return solution
