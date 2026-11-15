class Solution:
    def fib(self, n: int) -> int:
        hashing = {}
        def recursion(n):
            if n == 0:
                return 0 
            elif n == 1:
                return 1
            elif n in hashing:
                return hashing[n]
            else:
                f = recursion(n - 1)
                s = recursion(n - 2)
                hashing[n] = f + s
                return f + s

        return recursion(n)