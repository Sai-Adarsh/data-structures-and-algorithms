class MyCalendar:

    def __init__(self):
        
        self.L = []
        

    def book(self, start: int, end: int) -> bool:
        can_do = True
        if not self.L:
            self.L.append([start, end])
        else:
            for i, j in self.L:
                
                if i < start < j or i < end < j:
                    can_do = False
                    break
                elif start < i < end or start < j < end:
                    can_do = False
                    break
                elif [start, end] == [i, j]:
                    can_do = False
                    break
        if can_do:
            self.L.append([start, end])
        return can_do
            
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)