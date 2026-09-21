class Solution:
    def resultArray(self, A: List[int], k: int) -> List[int]:
        res = freq = [0] * k

        for n in A:
            n %= k
            # print("n", n)
            cur = [0] * k
            cur[n] = 1
            # print("cur", cur)

            for x, y in enumerate(freq):
                cur[x * n % k] += y
                # print("updated", cur)

            freq = cur
            # print("freq", freq)
            for x, y in enumerate(freq):
                res[x] += y
            # print("res", res)
            # print("")

        return res