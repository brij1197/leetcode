class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -inf
        if len(nums)>1:
            for i in range(1,len(nums)):
                nums[i]=max(nums[i]+nums[i-1],nums[i])
        return max(nums)