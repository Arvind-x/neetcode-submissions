class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in range(0,len(strs)):
            enc = enc + "'a'" + strs[i]
        return enc

    def decode(self, s: str) -> List[str]:
        k = s.split("'a'")
        k.pop(0)
        return k
