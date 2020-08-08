class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start < end:
            mid = math.floor((start+end)/2)

            if nums[mid] > nums[end]:
                start = mid+1

            else:
                end = mid

        return nums[start]
