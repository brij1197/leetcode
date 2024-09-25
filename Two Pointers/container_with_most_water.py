class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        max_res=0
        
        while left<=right:
            max_res=max(max_res,(right-left)*min(height[right],height[left]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_res