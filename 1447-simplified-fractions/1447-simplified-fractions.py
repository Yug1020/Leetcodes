class Solution:
    def gcd(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a if b == 0 else b
            
    def simplifiedFractions(self, n: int) -> List[str]:
    # my code
        # ans = set()
        # output = []
        # for numerator in range(1, n):
        #     for denominator in range(2, n+1):
        #         if ((numerator/denominator) < 1) and (numerator/denominator) not in ans:
        #             ans.add(numerator/denominator)
        #             output.append(f"{numerator}/{denominator}")

        # return output
    # best solution
        # denominator ranges from 2 to n
        # numerator ranges from 1 to n - 1
        result = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if gcd(numerator, denominator) == 1:
                    result.append(f"{numerator}/{denominator}")
        return result    
