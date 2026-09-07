class Solution:
    def firstUniqChar(self, s: str) -> int:
        h1 = {}
        for i in range(len(s)):
            element = s[i]

            if element in h1:
                h1[element][0] += 1
                h1[element][1] = i
            else:
                h1[element] = [1, i]
        
        for key, (count, last_index) in h1.items():
            if count == 1:
                return last_index

        return -1