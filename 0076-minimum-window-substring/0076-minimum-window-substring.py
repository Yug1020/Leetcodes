class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashing = {}

        for i in range(len(t)):
            if t[i] not in hashing:
                hashing[t[i]] = 1
            else:
                hashing[t[i]] += 1
        
        left = 0
        right = 0
        tarCount = 0
        minLen = float("inf")
        lastInd = -1

        while right < len(s):
            # print("s[right]=", s[right])
            if s[right] in hashing:
                if hashing[s[right]] > 0:
                    tarCount += 1
                hashing[s[right]] -= 1
            else:
                hashing[s[right]] = -1

            while tarCount == len(t):
                # print("hashing=", hashing)

                # print("minLen=", minLen)
                if s[left] in hashing:
                    hashing[s[left]] += 1
                    # print("internal", hashing[s[left]])
                    if hashing[s[left]] > 0:
                        # print(s[left], "is in hashing")
                        tarCount -= 1
                    # print("tarCount=", tarCount)

                # print("lastInd=", s[lastInd])
                # print("s[left]=", s[left])
                # print("")
                if right - left + 1 < minLen:
                    minLen = right - left + 1                
                    lastInd = left
                left += 1

            right += 1
        
        if lastInd == -1:
            return ""
        else:
            return s[lastInd: lastInd + minLen]