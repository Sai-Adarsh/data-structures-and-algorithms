class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        def DFS(node: int):
            if self.visited[node] == -1:
                return False

            if self.visited[node] == 1:
                return True
            
            self.visited[node] = -1

            for course in self.a_list[node]:
                if not DFS(course):
                    return False

            self.visited[node] = 1
            self.ret.append(node)
            return True
        
        self.visited = [0] * numCourses
        
        self.a_list = {x:[] for x in range(numCourses) }
        for course, prereq in prerequisites:
            self.a_list[prereq].append(course)

        self.ret = []
        for course in range(numCourses):
            if not DFS(course):
                return []

        return self.ret[::-1]