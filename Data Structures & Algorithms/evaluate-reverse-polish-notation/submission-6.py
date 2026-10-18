class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens.reverse() #O(n)
        op = {"+" : 1, "-" : 2, "*" : 3, "/" : 4}
        temp = []
        final = 0
        if len(tokens) == 1:
            return int(tokens[-1])
        while len(tokens) != 0:
            if tokens[-1] not in op:
                temp.append(tokens.pop(-1))
            else:
                a = int(temp.pop(-1))
                b = int(temp.pop(-1))
                if tokens[-1] == "+":
                    final = b + a
                elif tokens[-1] == "-":
                    final = b - a
                elif tokens[-1] == "*":
                    final = b * a
                else:
                    final = int(b / a)
                tokens.pop(-1)
                if len(tokens) != 0:
                    tokens.append(final)
        return final
            




        