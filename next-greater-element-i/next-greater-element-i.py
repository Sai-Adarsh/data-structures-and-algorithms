class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        for each in nums1:
            index_ = nums2.index(each)
            temp = [i for i in nums2[index_ : ] if i > each]
            if temp:
                res.append(temp.pop(0))
            else:
                res.append(-1)
                
        return(res)
            
        