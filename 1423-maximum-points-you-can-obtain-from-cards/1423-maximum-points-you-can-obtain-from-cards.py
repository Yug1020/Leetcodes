class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints) - 1
        left_sum = sum(cardPoints[0:k])
        right_sum = 0

        output = left_sum

        if len(cardPoints) == k:
            return sum(cardPoints)

        right = k
        left = 0

        for i in range(k + 1):
            calc = left_sum + right_sum
            output = max(output, calc)

            right -= 1
            left -= 1
            left_sum -= cardPoints[right]
            right_sum += cardPoints[left]

        return output