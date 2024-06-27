class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-1,0,-1):
            curr=nums[i]
            next=nums[i-1]
            if next<curr:
                nums[i:]=nums[n-1:i-1:-1]
                k=i
                while next>=nums[k]:
                    k+=1
                nums[i-1],nums[k]=nums[k],next
                return
        nums[0:]=nums[::-1]
                    