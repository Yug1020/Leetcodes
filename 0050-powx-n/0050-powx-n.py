class Solution:
    def mySqur(self, x, n, remainder):
        
        # print("x", x, "n", n, "remainder", remainder)
        if n > 1:
            if n % 2  == 0:
                # print("enter")
                return self.mySqur(x*x, n // 2, remainder)
            else:
                remainder = remainder * x
                return self.mySqur(x*x, n//2, remainder)
        else:
            output = x*remainder
            # print("output", output)
            return output

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        if n > 0:
            # print("n is", n, "which is grt than 0")
            return self.mySqur(x, n, 1)
        if n < 0: 
            # print("n is", n, "which is less than 0")            
            result = self.mySqur(x, abs(n), 1)
            return 1/result
