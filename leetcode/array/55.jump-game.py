def canJump(nums):
    if len(nums) == 1:
        return True
    if nums[-1] == 0:
        return True
    for i in range(len(nums)):
        if i == len(nums) - 1 and (nums[i] == len(nums)+1 or nums[i] % (len(nums)+1) == 0):
            return True
        if i == 0 and nums[i] % (len(nums)-1) == 0 and nums[i] != 0:
            return True
        if i == len(nums) - 1:
            i = -1
        if nums[i] + i + 1 == len(nums):
            return True
    return False


print(canJump([0, 2, 3]))
