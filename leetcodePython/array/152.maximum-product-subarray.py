def maxProduct(nums):
    r = nums[0]
    maxValue = nums[0]
    minValue = nums[0]
    for i in range(1, len(nums)):
        temp = maxValue
        maxValue = max(nums[i], nums[i]*maxValue, nums[i]*minValue)
        minValue = min(nums[i], nums[i]*temp, nums[i]*minValue)

        r = max(maxValue, r)

    return r


arr = [-5, 3, -4, -1, 7, 9]
print(maxProduct(arr))
