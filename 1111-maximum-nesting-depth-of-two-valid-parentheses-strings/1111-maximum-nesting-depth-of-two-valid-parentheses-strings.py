class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        curr_depth = 0
        res = []

        for i in seq:
            if curr_depth > depth:
                depth = curr_depth
            if i == "(":
                curr_depth += 1
            if i == ")":
                curr_depth -= 1

        threshold = depth // 2

        curr_state = 0
        for i in range(len(seq)):
            if seq[i] == "(":
                curr_state += 1
            if curr_state <= threshold:
                res.append(0)
            else:
                res.append(1)
            if seq[i] == ")":
                curr_state -= 1

        return res