class Solution:
    def isValid(self, s: str) -> bool:
        st1 = list(s)
        st2 = []
        ins = {"{":"}", "[":"]", "(":")"}
        if len(s) % 2 == 1:
            return False
        while len(st1) != 0:
            if len(st2) != 0 and st1[-1] in ins:
                if st2[-1] != ins[st1[-1]]:
                    return False
                else:
                    st1.pop(-1)
                    st2.pop(-1)
            else:
                st2.append(st1[-1])
                st1.pop(-1)
        if len(st2) != 0:
            return False
        return True

        