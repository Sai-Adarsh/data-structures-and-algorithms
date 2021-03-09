class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        one = 0
        two = 0
        res = []
        
        while one < len(firstList) or two < len(secondList):
            try:
                if firstList[one][0] <= secondList[two][1] and firstList[one][1] >= secondList[two][0]:
                    res.append([max(firstList[one][0], secondList[two][0]), min(firstList[one][1], secondList[two][1]) ])
                if firstList[one][1] > secondList[two][1]:
                    two += 1
                else:
                    one += 1
            except:
                break
        return res