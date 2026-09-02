class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for letter in s:
            if letter in dict_s:
                dict_s[letter]+=1
            else:
                dict_s[letter] = 1
        for letter in t:
            if letter in dict_s:
                dict_s[letter]-=1
            else:
                return False
        for i in dict_s.keys():
            if dict_s[i] != 0:
                return False
        return True


        

       