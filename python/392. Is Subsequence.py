class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t=iter(t)
        for char in s:
            if char not in t:
                return False
        return True