class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr = []

        for i in s:
            if i == "(":
                arr.append(i)
            if i == ")" and len(arr) > 0 and arr[len(arr) - 1] == "(":
                arr.pop()
            elif i == ")":
                arr.append(i)
            
        return len(arr)