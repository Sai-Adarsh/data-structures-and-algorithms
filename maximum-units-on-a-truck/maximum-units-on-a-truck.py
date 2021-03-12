class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        res = 0

        for i in boxTypes:
            if i[0] > truckSize:
                units_to_be_added = min(i[0], truckSize)
                res += units_to_be_added * i[1]
                break
            else:
                truckSize = truckSize - i[0]
                res += i[0] * i[1]
        return res