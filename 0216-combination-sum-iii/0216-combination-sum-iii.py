class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if n == 0 or n == 1:
            return []
        
        can = []
        for i in range(1, 10):
            can.append(i)

        output = []
        target = n
        n = len(can)
        
        def recursion(ind, arr, total):
            if total == target and len(arr) == k:
                output.append(arr[:])
                return

            if ind >= n or total >= target:
                return
            
            arr.append(can[ind])
            left = recursion(ind + 1, arr, total + can[ind])

            arr.pop()
            right = recursion(ind + 1, arr, total)

        recursion(0, [], 0)
        return output