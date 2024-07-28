class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums:
            mid=len(nums)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return self.searchInsert(nums[:mid],target)
            else:
                return self.searchInsert(nums[mid+1:],target)+mid+1
        else:
            return 0