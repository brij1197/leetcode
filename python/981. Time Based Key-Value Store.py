class TimeMap:

    def __init__(self):
        self.timemap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=[]
        self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result=""
        values=self.timemap.get(key,[])
        low,high=0,len(values)-1
        while low<=high:
            mid=low+(high-low)//2
            if values[mid][1]<=timestamp:
                result=values[mid][0]
                low=mid+1
            else:
                high=mid-1
        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)