class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        output = 0
        curr_len = 0
        maxF = 0
        fCount = {}
        left = 0

        for i in range(n):
            if s[i] in fCount:
                fCount[s[i]] += 1
            else:
                fCount[s[i]] = 1

            if fCount[s[i]] > maxF:
                maxF = fCount[s[i]]

            while (i - left + 1) - maxF > k:
                fCount[s[left]] -= 1
                left += 1

            curr_len = i - left + 1
            if curr_len > output:
                output = curr_len
            
        return output