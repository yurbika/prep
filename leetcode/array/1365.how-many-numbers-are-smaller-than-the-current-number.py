class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or not nums:
            return
        solution = []
        for i in nums:
            cnt = 0
            for j in nums:
                if i > j:
                    cnt += 1

            solution.append(cnt)

        return solution
