class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [0]
        stack = [0]
        
        while stack:
            node = stack.pop()
            for neighbours in rooms[node]:
                if neighbours not in seen:
                    seen.append(neighbours)
                    stack.append(neighbours)
                    
        return len(seen) == len(rooms)