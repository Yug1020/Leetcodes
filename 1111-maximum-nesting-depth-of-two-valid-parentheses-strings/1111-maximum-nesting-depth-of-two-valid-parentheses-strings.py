class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:


        depth = 0
        res = [0] * len(seq)

        for i in range(len(seq)):
            if seq[i] == "(":
                depth += 1
            res[i] = depth % 2
            if seq[i] == ")":
                depth -= 1

        return res