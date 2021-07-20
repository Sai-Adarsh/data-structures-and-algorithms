class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        one = 0
        two = 0
        
        for i in range(len(arr1)):
            if arr1[i]:
                temp = (-2) ** i
                one += temp
                
        for i in range(len(arr2)):
            if arr2[i]:
                temp = (-2) ** i
                two += temp
                
        n = one + two
        res = [] if n else [0]
        while n:
            n, rem = divmod(n, -2)
            if rem < 0:
                n += 1
            res.append(abs(rem))
        res.reverse()
        return res