class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charset=set(s)
        for char in charset:
            if s.count(char)!=t.count(char):
                return False            
        return True