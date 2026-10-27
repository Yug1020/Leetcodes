class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0
        total = 0

        while left != right:
            if height[left] <= height[right]:
                if leftMax < height[left]:
                    leftMax = height[left]
                left += 1
                lastShift = "left"
            else:
                if rightMax < height[right]:
                    rightMax = height[right]
                right -= 1
                lastShift = "right"
            
            if lastShift == "left":
                calc = leftMax - height[left]
                if calc > 0:
                    total += calc
            else:
                calc = rightMax - height[right]
                if calc > 0:
                    total += calc

        return total