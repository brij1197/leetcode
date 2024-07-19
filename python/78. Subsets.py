class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sub=[],[]
        def backtrack(idx):
            if idx==len(nums):
                res.append(sub[:])
                return
            sub.append(nums[idx])
            backtrack(idx+1)
            sub.pop()
            backtrack(idx+1)
        backtrack(0)
        return res