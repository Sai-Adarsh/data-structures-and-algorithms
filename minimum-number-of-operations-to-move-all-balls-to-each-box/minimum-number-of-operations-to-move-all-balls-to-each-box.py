class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(i) for i in boxes]
        dp = []
        for i in range(len(boxes)):
            curr_res = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == 1:
                    curr_res += abs(i - j)
            dp.append(curr_res)
        return(dp)