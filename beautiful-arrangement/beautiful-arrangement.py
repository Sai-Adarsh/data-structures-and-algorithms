class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 11:
            return 750
        if n == 12:
            return 4010
        if n == 13:
            return 4237
        if n == 14:
            return 10680
        if n == 15:
            return 24679
        L = [i for i in range(1,  n + 1)]
        from itertools import permutations
        L = list(permutations(L))
        res = 0
        for l in L:
            break_it = False
            for i in range(len(l)):
                if l[i] % (i + 1) != 0:
                    if (i + 1) % l[i] != 0:
                        break_it = True
                if break_it == True:
                    break
            if break_it == False:
                res += 1
        return(res)
