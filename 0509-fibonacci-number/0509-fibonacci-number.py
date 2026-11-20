class Solution:
    def fib(self, n: int) -> int:
    #recursion solution

        # if n == 0 or n == 1:
        #     return n

        # maping = {}
        # def recursion(n, maping):
        #     if n == 0 or n == 1:
        #         return n
            
        #     if n in maping:
        #         return maping[n]

        #     f = recursion(n - 1, maping) 
        #     s = recursion(n - 2, maping)

        #     if n not in maping:
        #         maping[n] = f + s

        #     return f + s

        # return recursion(n, {})


    #tabulation solution
        
        if n <= 1:
            return n
        dp = [0, 1]

        for i in range(2, n+1):
            dp.append(dp[i - 1] + dp[i - 2])
        
        return dp[len(dp) - 1]
