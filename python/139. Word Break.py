class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for idx in range(len(s)-1,-1,-1):
            for word in wordDict:
                if s[idx:idx+len(word)]==word and (idx+len(word))<=len(s):
                    dp[idx]=dp[idx+len(word)]
                if dp[idx]:
                    break
        return dp[0]