from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        
        curList=self.d[key]
        if len(curList)==0:
            return ""
        low=0
        high=len(curList)-1
        
        while low<high:
            
            mid= low+ (high-low+1)//2
            
            if curList[mid][0]<=timestamp:
                low=mid
            else:
                high=mid-1
                
        if curList[low][0]<=timestamp:
            return curList[low][1]
        
        return ""
            
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)