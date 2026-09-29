class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str1 = {}
        for s in s1:
            if s in str1:
                str1[s] += 1
            else:
                str1[s] = 1

        n = len(s2)
        n0 = len(s1)
        found = defaultdict(int)

        if len(s1) > len(s2):
            return False

        for i in range(0, n0):
            found[s2[i]] += 1

        l = 0
        r = n0-1

        while r < n-1:
            if found == str1:
                return True
            else:
                found[s2[l]] -= 1
                if found[s2[l]] == 0:
                    found.pop(s2[l])
                l += 1
                r += 1
                found[s2[r]] += 1
        return found == str1
            
        