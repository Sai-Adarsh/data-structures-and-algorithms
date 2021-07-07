class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        stops = []
        
        for passengers, start, stop in  trips:
            stops.append([start, passengers])
            stops.append([stop, -passengers])
            
        stops.sort()    
        
        for location, passengers in stops:
            capacity -= passengers
            if capacity < 0:
                return False
            
        return True