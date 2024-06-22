class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]%=2
        
        prefix_arr=[0]*(len(nums)+1)
        prefix_arr[0]=1
        
        ans,summ=0,0
        
        for num in nums:
            summ+=num
            if summ>=k:
                ans+=nums[summ-k]
            prefix_arr[summ]+=1
        return ans