class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        map_dict = {}
        from collections import deque
        for i in groupSizes:
            if i not in map_dict:
                map_dict[i] = [deque([None for _ in range(i)])]

        count = 0
        for i in groupSizes:
            #print(map_dict[i], i, map_dict[i][-1])
            if map_dict[i][-1][-1] != None:
                map_dict[i].append(deque([None for _ in range(i)]))
                map_dict[i][-1].appendleft(count)
                map_dict[i][-1].pop()
            else:
                map_dict[i][-1].appendleft(count)
                map_dict[i][-1].pop()
            count += 1
        res = []
        L = map_dict.values()
        for i in L:
            for j in i:
                res.append(list(j))
        return(res)