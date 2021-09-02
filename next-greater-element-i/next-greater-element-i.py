class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        for each in nums1:
            is_there = nums2.index(each)
            poss = [i for i in nums2[is_there : ] if i > each]
            if poss:
                res.append(poss.pop(0))
            else:
                res.append(-1)
                
        return res