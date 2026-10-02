class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        hashing = {}
        left = 0
        right = 0
        maxLength = 0
        currLength = 0

        while right < len(s):
            if s[right] not in hashing:
                hashing[s[right]] = right
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                if s[right] in hashing:
                    if hashing[s[right]] >= left:

                        left = hashing[s[right]] + 1
                        # print("key", s[right], "val", right)
                        hashing[s[right]] = right

                        currLength = right - left + 1
                        maxLength = max(maxLength, currLength)
                    else:
                        hashing[s[right]] = right
                        currLength += 1
                        maxLength = max(maxLength, currLength)                        
            # print("right", right)
            # print("left", left)
            # print("s[right] => ", s[right])
            # print("hashing", hashing)
            # print("currLength", currLength)
            # print("")     

            right += 1

        return maxLength