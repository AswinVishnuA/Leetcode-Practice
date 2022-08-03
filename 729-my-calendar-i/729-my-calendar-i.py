from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        
        self.cal=SortedList([])

    def book(self, start: int, end: int) -> bool:
        n=len(self.cal)
        # print(start,end,self.cal)
        for i in range(n):
            cs,ce=self.cal[i]
            
            if not (end<=cs or ce<=start):
                return False
        
        self.cal.add([start,end])
        
        return True
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)