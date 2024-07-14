class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums=sorted(nums,reverse=True)
        total=sum(nums)
        if total%2==1:
            return False
        target=total//2
        
        dp=set([0])
        
        for num in nums:
            if target-num in dp:
                return True
            
            dp.update([val+num for val in dp])
        
        return False