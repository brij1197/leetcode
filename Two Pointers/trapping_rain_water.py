class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        left,right=height[i],height[j]
        res=0
        while i<j:
            if left<=right:
                res+=left-height[i]
                i+=1
                left=max(left,height[i])
            else:
                res+=right-height[j]
                j-=1
                right=max(right,height[j])
        return res