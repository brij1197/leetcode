class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxx=0
        for num in nums:
            x=num-1
            result=0
            if x not in nums:
                while x+1 in nums:
                    x+=1
                    result+=1
                maxx=max(maxx, result)
        return maxx