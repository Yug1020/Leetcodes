class Solution:
    def fib(self, n: int) -> int:
        def recursion(n):
            if n == 0 or n == 1:
                return n
            
            n = recursion(n - 1) + recursion(n - 2)

            return n

        return recursion(n)