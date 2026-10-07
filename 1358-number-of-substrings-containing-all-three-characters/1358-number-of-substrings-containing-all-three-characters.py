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

#previous logic

# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         output: int = 0
#         left: int = 0
#         a: int = 0
#         b: int = 0
#         c: int = 0
#         n: int = len(s)
#         acc: int = 0
#         for i in range(n):
#             print("i=", i,"is=", s[i])

#             if s[i] == 'a': a += 1
#             elif s[i] == 'b': b += 1
#             else: c += 1
#             while a and b and c:
#                 if s[left] == 'a': a -= 1
#                 elif s[left] == 'b': b -= 1
#                 else: c -= 1
#                 acc += 1
#                 left += 1
#                 # print("acc", acc)
#             output += acc
#             print("left=", left)
#             print("a=", a)
#             print("b=", b)
#             print("c=", c)
#             print("acc", acc)
#             print("output=", output)
#             print("")
#             # print("output", output)
#         return output