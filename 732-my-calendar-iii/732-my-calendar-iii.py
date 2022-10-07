from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.d=SortedDict()

    def book(self, start: int, end: int) -> int:
        
        self.d[start]=self.d.get(start,0)+1
        
        self.d[end]=self.d.get(end,0)-1
        
        
        cur=0
        curMax=0
        for value in self.d.values():
            cur+=value
            curMax=max(cur,curMax)
        
        return curMax
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)