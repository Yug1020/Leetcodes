class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = set()
        output = []
        for numerator in range(1, n):
            for denominator in range(2, n+1):
                if ((numerator/denominator) < 1) and (numerator/denominator) not in ans:
                    ans.add(numerator/denominator)
                    output.append(f"{numerator}/{denominator}")

        return output