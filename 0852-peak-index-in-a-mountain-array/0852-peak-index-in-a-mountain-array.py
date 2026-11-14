# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         n = len(arr)
#         mid = n // 2

#         while arr[mid + 1] and arr[mid] < arr[mid + 1]:
#             mid = mid + 1
            
#         while arr[mid - 1] and arr[mid] < arr[mid - 1]:
#             mid = mid - 1

#         return mid

#     #another way to solve this problem
#         # return arr.index(max(arr))

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If we are on the rising slope, the peak is to the right
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            # If we are on the falling slope, the peak is at mid or to the left
            else:
                right = mid
                
        return left