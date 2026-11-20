class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        maping = {}
        def recursion(n, maping):
            if n == 0 or n == 1:
                return n
            
            if n in maping:
                return maping[n]

            f = recursion(n - 1, maping) 
            s = recursion(n - 2, maping)

            if n not in maping:
                maping[n] = f + s

            return f + s

        return recursion(n, {})