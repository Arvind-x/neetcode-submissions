class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =[]
        temp = []
        maxFound = 0
        while len(temperatures) != 0:
            t = temperatures[-1]
            found = 0
            exp = len(temp)
            j = exp -1
            k = 1
            Found = False
            while j >= 0:
                if temp[j] > t:
                    Found = True
                    result.append(k)
                    break
                else:
                    k +=1
                j-=1
            if not Found:
                result.append(0)
            if temperatures[-1] >= maxFound:
                maxFound = temperatures[-1]
                temp = []
            temp.append(temperatures.pop(-1))
        result.reverse()
        return result




        