class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(n):
            if n==len(nums):
                result.append(nums[:])
            for i in range(n, len(nums)):
                nums[i],nums[n]=nums[n],nums[i]
                backtrack(n+1)
                nums[i],nums[n]=nums[n],nums[i]
        backtrack(0)
        return result