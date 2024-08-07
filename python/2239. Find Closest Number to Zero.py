class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        small=nums[0]
        for num in nums:
            if abs(num)<abs(small):
                small=num
            elif abs(num)==abs(small) and num > small:
                small=num
        return small