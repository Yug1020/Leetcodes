class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def sum_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return

            if idx >= len(candidates) or total > target:
                return 

            comb.append(candidates[idx])
            sum_combination(idx, comb, total + candidates[idx])

            comb.pop()
            sum_combination(idx + 1, comb, total)

            return res

        return sum_combination(0, [], 0)