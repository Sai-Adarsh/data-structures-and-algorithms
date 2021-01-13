class Solution:
    def minSteps(self, s: str, t: str) -> int:
        to_be_checked = []
        for i in s:
            if i in t:
                if i not in to_be_checked:
                    to_be_checked.append(i)
​
        from collections import Counter
        s_c = Counter(s)
        t_c = Counter(t)
​
        res = 0
        for i in to_be_checked:
            res += min(s_c[i], t_c[i])
        return(len(s) - res)
