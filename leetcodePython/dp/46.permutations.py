class Solution:
    def createPermutations(self, arr, num):
        temp = []
        if len(arr) == 1:
            temp.append([arr[0], num])
            temp.append([num, arr[0]])
        else:
            for ele in arr:
                for i in range(len(ele)+1):
                    if i == 0:
                        temp.append([num] + ele[:])
                    elif i == len(arr):
                        temp.append(ele[:]+[num])
                    else:
                        temp.append(ele[:i]+[num]+ele[i:])

        return temp

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return self.createPermutations([nums[0]], nums[1])

        return self.createPermutations(self.permute(nums[:-1]), nums[-1])
