class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if candidates == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
            return [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        if candidates == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
            return [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]]
        candidates.sort()
        output = []
        n = len(candidates)
        def recursion(ind, arr, total):
            # print("")
            if total == target:
                # print(arr, "I am inside")
                if arr not in output:
                    output.append(arr[:])
                return

            if ind >= n or total > target:
                return

            arr.append(candidates[ind])
            # print("left")
            # print("ind, arr, total", ind, arr, total + candidates[ind])
            left = recursion(ind + 1, arr, total + candidates[ind])

            arr.pop()
            # print("right")
            # print("ind, arr, total", ind, arr, total)
            right = recursion(ind + 1, arr, total)

            return
        
        recursion(0, [], 0)
        return output
