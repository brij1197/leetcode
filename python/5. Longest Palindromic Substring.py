class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if s[::-1]==s:
            return s
        
        def expand(s,left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1
        
        start,end=0,0
        
        for i in range(len(s)):
            odd_length=expand(s,i,i)
            even_length=expand(s,i,i+1)
            max_length=max(odd_length,even_length)
            
            if max_length>end-start:
                start=i-(max_length-1)//2
                end=i+max_length//2
        return s[start:end+1]