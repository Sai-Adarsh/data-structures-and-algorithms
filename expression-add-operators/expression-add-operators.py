class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backTracking(res, curr_path, start):
            if start == len(num):
                temp = "".join(curr_path)
                if eval(temp) == target:
                    res.append(temp)
                return

            for i in range(start + 1, len(num) + 1):
                sub_string = num[start : i]
                if len(sub_string) == len(str(int(sub_string))):
                    if not curr_path:
                        backTracking(res, curr_path + [sub_string], i)
                    else:
                        poss = ["+", "*", "-"]
                        for each in poss:
                            backTracking(res, curr_path + [each] + [sub_string], i)
                else:
                    continue
            return res
        L = backTracking([], [], 0)
        return L