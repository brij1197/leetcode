class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=[[idx,num] for idx,num in enumerate(nums)]
        nums=sorted(nums,key=lambda x:x[1])
        left,right=0,len(nums)-1
        while left<right:
            if nums[left][1]+nums[right][1]>target:
                right-=1
            elif nums[left][1]+nums[right][1]<target:
                left+=1
            else:
                return nums[left][0],nums[right][0]