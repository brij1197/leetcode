class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        roman_val={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result=0
        
        for a,b in zip(s,s[1:]):
            if roman_val[a]<roman_val[b]:
                result-=roman_val[a]
            else:
                result+=roman_val[a]
        return result+roman_val[s[-1]]