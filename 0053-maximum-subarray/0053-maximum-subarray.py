class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        cur= 0
        b  = float('-inf')
        for i in nums:
            cur+=i
            if cur<=i:
                cur=i

            if cur>b:
                b=cur

        return b