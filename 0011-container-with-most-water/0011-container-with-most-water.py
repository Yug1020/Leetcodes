class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height) - 1
        left = 0
        right = n
        prod = 0
        # itr = 0
        while right != left:
            # print("itr", itr)
            # print("left", left, "right", right)
            if height[right] < height[left]:
                h = height[right]
            else:
                h = height[left]
            
            currLen = right - left
            # print("currLen", currLen, "h", h, "multi", currLen * h)
            if (currLen * h) > prod:
                prod = currLen * h
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

            # itr += 1
            # print("")

        return prod