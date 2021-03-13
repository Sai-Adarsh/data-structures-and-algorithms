class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        a_ptr = 0
        b_ptr = 0
        
        res = []
        
        while a_ptr < len(firstList) or b_ptr < len(secondList):
            try:
                if firstList[a_ptr][0] <= secondList[b_ptr][1] and firstList[a_ptr][1] >= secondList[b_ptr][0]:
                    res.append([max(firstList[a_ptr][0], secondList[b_ptr][0]), min(firstList[a_ptr][1], secondList[b_ptr][1])])
                if firstList[a_ptr][1] > secondList[b_ptr][1]:
                    b_ptr += 1
                else:
                    a_ptr += 1
            except:
                break
        return res