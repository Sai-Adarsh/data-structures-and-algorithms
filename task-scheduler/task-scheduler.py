class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        hash_map = collections.Counter(tasks)
        
        max_freq = max(hash_map.values())
        count = 0
        for i, j in hash_map.items():
            if j == max_freq:
                count += 1
                
        return max((max_freq - 1) * (n + 1) + (count), len(tasks))