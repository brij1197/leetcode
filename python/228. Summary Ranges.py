class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result=[]
        i=0
        while i<len(nums):
            first=nums[i]
            while i<len(nums)-1 and nums[i]+1==nums[i+1]:
                i+=1
            if first!=nums[i]:
                result.append(str(first)+"->"+str(nums[i]))
            else:
                result.append(str(nums[i]))
            i+=1
        return result