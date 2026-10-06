class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        curr_len = 0
        max_len = 0
        buckets = {}
        left = 0
        right = 0

        while right < len(fruits):
            if fruits[right] not in buckets:
                buckets[fruits[right]] = 1
                curr_len += 1
            else:
                buckets[fruits[right]] += 1
                curr_len += 1
            
            if len(buckets) > 2:
                while len(buckets) > 2:
                    buckets[fruits[left]] -= 1
                    if buckets[fruits[left]] == 0:
                        del buckets[fruits[left]]
                    left += 1
                    curr_len -= 1

            if curr_len > max_len:
                max_len = curr_len

            right += 1
        
        return max_len