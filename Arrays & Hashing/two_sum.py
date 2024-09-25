class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums=[(val,idx) for idx,val in enumerate(nums)]
        nums=sorted(nums,key=lambda x:x[0])
        left,right=0,len(nums)-1
        while left<=right:
            if nums[left][0]+nums[right][0]<target:
                left+=1
            elif nums[left][0]+nums[right][0]>target:
                right-=1
            else:
                return nums[left][1],nums[right][1]