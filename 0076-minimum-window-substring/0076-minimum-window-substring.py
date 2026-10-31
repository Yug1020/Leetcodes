class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        left = 0 
        right = 0
        hashing = {}
        comp = {}
        have = 0
        need = 0
        output = [float("inf"), [-1, -1]]

        for i in range(len(t)):
            if t[i] not in hashing:
                hashing[t[i]] = 1
            else:
                hashing[t[i]] += 1
            
        need = len(hashing)

        # print("need =", need)
        # print("hashing =", hashing)
        # print("")

        while right < len(s):
            # print("left =", left, "right =", right)
            # print("s[left] =", s[left], "s[right] =", s[right])

            if s[right] in hashing:
                if s[right] not in comp:
                    comp[s[right]] = 1
                    if comp[s[right]] == hashing[s[right]]:
                        have += 1
                else:
                    comp[s[right]] += 1
                    if comp[s[right]] == hashing[s[right]]:
                        have += 1                    

            # print("comp =", comp)
            # print("have =", have)

            while have == need:
                curr = right - left + 1

                if output[0] > curr:
                    output[0] = curr
                    output[1] = [left, right]
                
                if left <= right and have == need:
                    if s[left] in comp:
                        comp[s[left]] -= 1
                        if comp[s[left]] == 0:
                            del comp[s[left]]
                            have -= 1
                    if s[left] in comp and comp[s[left]] < hashing[s[left]]:
                        have -= 1

                # print("comp =", comp)
                # print("have =", have)

                left += 1
            
            # print("output", output)
            right += 1
            # print("")
        
        return s[output[1][0] : output[1][1] + 1]