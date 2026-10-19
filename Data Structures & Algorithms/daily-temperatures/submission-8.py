class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        i = len(temperatures) - 2
        he = 0
        while i >= 0:
            
            if temperatures[i+1] > temperatures[i]:
                res[i] = 1
            elif res[i+1] == 0:
                res[i] = 0
            else:
                j = i + 1
                found = False
                while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                    
                    if res[j] == 0:
                        found = False
                        break
                    j = j + res[j]
                    if temperatures[j] > temperatures[i]:
                        found = True
                if found:
                    res[i] = j - i
                else:
                    res[i] = 0
            i-=1
        return res

                
                    