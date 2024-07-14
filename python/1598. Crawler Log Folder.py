class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result=0
        for log in logs:
            if log=='../':
                result-=1 if result>0 else 0
            elif log=='./':
                pass
            else:
                result+=1
        return result