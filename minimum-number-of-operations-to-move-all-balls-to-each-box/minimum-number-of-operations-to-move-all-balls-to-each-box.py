class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        # Naive brute force solution O(N ** 2)
        boxes = [int(i) for i in boxes]
        res = [0 for _ in range(len(boxes))]
        
        for i in range(len(boxes)):
            temp = 0
            for j in range(len(boxes)):
                if i != j:
                    if boxes[j]:
                        temp += abs(i - j)
            res[i] = temp
        return res