class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        maxval=0
        for num in numsset:
            x=num-1
            current=0
            if x not in numsset:
                while x+1 in numsset:
                    x+=1
                    current+=1
                maxval=max(maxval,current)
        return maxval