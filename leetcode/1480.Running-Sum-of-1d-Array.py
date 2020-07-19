class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        for i in range(len(nums)):
            temp.append(sum(nums))
            nums.pop(len(nums)-1)
        
        temp.reverse()
        return temp