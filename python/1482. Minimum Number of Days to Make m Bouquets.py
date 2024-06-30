class Solution: 
    def possible(self,bloomDay,mid,m,k):
        flowers,bouquets=0,0
        for bloom in bloomDay:
            if bloom>mid:
                flowers=0
            else:
                bouquets+=(flowers+1)//k
                flowers=(flowers+1)%k
        return bouquets>=m
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        left,right=1,max(bloomDay)
        while left<right:
            mid=left+(right-left)//2
            if self.possible(bloomDay,mid,m,k):
                right=mid
            else:
                left=mid+1
        return left