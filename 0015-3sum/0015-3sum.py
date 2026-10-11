# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         output = []
#         nums.sort()

#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             left = i + 1
#             right = len(nums) - 1
            
#             while left < right:
#                 add = nums[i] + nums[left] + nums[right]

#                 if add > 0:
#                     right -= 1
                
#                 elif add < 0:
#                     left += 1
                
#                 else:
#                     output.append([nums[i], nums[left], nums[right]])

#                     while nums[left] == nums[left - 1] and left < right:
#                         left += 1
                    
#         return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res