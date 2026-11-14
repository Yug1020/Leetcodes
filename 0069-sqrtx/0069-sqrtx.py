class Solution(object):
    def mySqrt(self, x):
        # if x < 2:
        #     return x
        
        # i = 2
        # while i * i <= x:
        #     i += 1
        
        # return i - 1

        if x < 2:
            return x

        low = 1
        high = x
        output = float("-inf")

        while low <= high:
            mid = (low + high) // 2

            if mid*mid <= x:
                low = mid + 1
                if mid > output:
                    output = mid
            
            elif mid*mid > x:
                high = mid - 1

        return output
