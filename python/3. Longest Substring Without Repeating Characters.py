class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=result=0
        substr=set()
        
        for right in range(len(s)):
            while s[right] in substr:
                substr.remove(s[left])
                left+=1
            substr.add(s[right])
            result=max(result,len(substr))
        return result