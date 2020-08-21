class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxValue = -1
        while i < j:
            minValue = min(height[i], height[j])
            maxValue = max(maxValue, minValue*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxValue
