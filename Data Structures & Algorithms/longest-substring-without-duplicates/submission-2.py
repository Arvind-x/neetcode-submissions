class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l = 0
        r = 0
        if len(s) <= 1:
            return len(s)
        found = {}
        for r in range(0, len(s)):
            if s[r] not in found or found[s[r]] < l:
                found[s[r]] = r
                maxlen = max(maxlen, r - l +1)
            else:
                l = found[s[r]] + 1
                found[s[r]] = r

            
        return maxlen


        