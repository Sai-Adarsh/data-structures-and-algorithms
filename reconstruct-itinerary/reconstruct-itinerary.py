class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)
        stack = ['JFK']
        path = []
        while stack:
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                path.append(stack.pop())
        return path[::-1]