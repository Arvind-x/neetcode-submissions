class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [letter for letter in s if letter.isalnum()]
        l = 0
        r = len(new) - 1
        print(new)
        while l < r:
            while not new[l].isalnum():
                l+=1
            while not new[r].isalnum():
                r-=1
            if new[l].lower() != new[r].lower():
                return False
            l+=1
            r-=1
        return True 
                
                

        