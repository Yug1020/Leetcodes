class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        max_char = 0
        left = 0
        char = [-1, -1, -1]

        while left < n:
            char[ord(s[left]) - ord("a")] = left

            if char[0] > -1 and char[1] > -1 and char[2] > -1:
                max_char += min(char[0], char[1], char[2]) + 1


            left += 1

        return max_char