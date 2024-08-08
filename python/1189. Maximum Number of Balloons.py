class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        result='balloon'
        res_hash={i:0 for i in set(result)}
        
        for i in res_hash:
            res_hash[i]+=int(text.count(i)/result.count(i))
        return min(res_hash.values())