from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result=defaultdict(int)
        for i in s: result[i]+=1
        for i in t: result[i]-=1
        return all(x==0 for x in result.values())