class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        maxlen = 0
        freqs = {}
        while r < n:
            if s[r] in freqs:
                freqs[s[r]] += 1
            else:
                freqs[s[r]] = 1
            max_freq = max(freqs.values())
            if r - l + 1 - max_freq <= k:
                maxlen = max(r - l + 1, maxlen)
                r += 1
            else:
                freqs[s[r]] -= 1
                freqs[s[l]] -= 1
                l += 1



        return maxlen





        