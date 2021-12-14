class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        hashMap = collections.Counter(tasks)
        maxCount = max(hashMap.values())
        count = 0
        
        for i, j in hashMap.items():
            if j == maxCount:
                count += 1
                
        return max((maxCount - 1) * (n + 1) + count, len(tasks))