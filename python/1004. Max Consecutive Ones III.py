class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,numzeroes,maxx=0,0,0
        for right in range(len(nums)):
            if nums[right]==0:
                numzeroes+=1
            while numzeroes>k:
                if nums[left]==0:
                    numzeroes-=1
                left+=1
            maxx=max(right-left+1,maxx)
        return maxx