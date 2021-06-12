class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        backup_len = len(arr)
        res = []
        for i in arr:
            if i == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(i)
                
        arr[:] = res[:backup_len]
                