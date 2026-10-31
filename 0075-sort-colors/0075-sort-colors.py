class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red = 0
        # white = red + 1
        # blue = red + 2

        # for i in range(len(nums)):
        #     while red < len(nums) - 1 and nums[red] == 0:
        #         red += 1
        #     while white < len(nums) - 1 and nums[white] == 1:
        #         white += 1
        #     while blue < len(nums) - 1 and nums[blue] == 2:
        #         blue += 1
            
        #     if nums[i] == 0 and red < len(nums) - 1 and nums[red] != 0:
        #         nums[i], nums[red] = nums[red], nums[i]
        #         red += 1
            
        #     if nums[i] == 1 and white < len(nums) - 1 and nums[white] != 1:
        #         nums[i], nums[white] = nums[white], nums[i]
        #         white += 1
            
        #     if nums[i] == 2 and blue < len(nums) - 1 and nums[blue] != 2:
        #         nums[i], nums[blue] = nums[blue], nums[i]
        #         blue += 1



        # i = 0

        # while i < len(nums):

        #     if nums[i] == 0 and red < len(nums) and nums[red] != 0:
        #         print("nums[i]", nums[i], "i", i, "nums[red]", nums[red], "red", red)
        #         nums.insert(red, nums.pop(i))
        #         print("nums by red", nums)
        #         red += 1
        #         continue

        #     elif nums[i] == 1 and white < len(nums) and nums[white] != 1:
        #         print("nums[i]", nums[i], "i", i, "nums[white]", nums[red], "red", red)                
        #         nums.insert(white, nums.pop(i))
        #         print("nums by white", nums)
        #         white += 1
        #         continue
            
        #     elif nums[i] == 2 and blue < len(nums) and nums[blue] != 2:
        #         print("nums[i]", nums[i], "i", i, "nums[blue]", nums[red], "red", red)
        #         nums.insert(blue, nums.pop(i))
        #         print("nums by blue", nums)
        #         blue += 1
        #         continue
            
        #     i += 1
        #     print("")

        # if len(nums) == 1:
        #     return nums

        # start = 0
        # middle = 0
        # end = len(nums) - 1

        # while middle <= end:
        #     if nums[middle] == 2:
        #         nums[middle], nums[end] = nums[end], nums[middle]
        #         end -= 1
            
        #     if middle <= end and middle == start and nums[middle] == 0:
        #         middle += 1
        #         start += 1
            
        #     if middle != start and nums[middle] == 0:
        #         nums[start], nums[middle] = nums[middle], nums[start]
        #         middle += 1
        #         start += 1
            
        #     if middle <= end and nums[middle] == 1:
        #         middle += 1
        
        # print("nums", nums)

        if len(nums) == 1:
            return nums

        r0 = 0
        r1 = 0
        r2 = len(nums) - 1

        while r1 <= r2:
            if r1 <= r2 and nums[r1] == 2:
                nums[r1], nums[r2] = nums[r2], nums[r1]
                while nums[r2] == 2 and r2 > -1:
                    r2 -= 1
            
            if r0 == r1 and r1 <= r2 and nums[r1] == 0:
                r0 += 1
                r1 += 1
            
            if r0 != r1 and r1 <= r2 and nums[r1] == 0:
                nums[r0], nums[r1] = nums[r1], nums[r0]
                r0 += 1
                r1 += 1
            
            if r1 <= r2 and nums[r1] == 1:
                r1 += 1