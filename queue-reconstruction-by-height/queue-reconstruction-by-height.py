class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        
        for each_person in people:
            res.insert(each_person[1], each_person)
            
        return res