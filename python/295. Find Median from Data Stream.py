class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        left,right=0,len(self.arr)
        while left<right:
            mid=(left+right)//2
            
            if self.arr[mid]>num:
                right=mid
            else:
                left=mid+1
        self.arr.insert(left,num)

    def findMedian(self) -> float:
        n=len(self.arr)
        if n%2==1:
            return self.arr[n//2]
        else:
            return (self.arr[n//2-1]+self.arr[n//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()