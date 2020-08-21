class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        solution = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax:
                solution += leftMax - height[left]
                left += 1
            else:
                solution += rightMax - height[right]
                right -= 1

        return solution
