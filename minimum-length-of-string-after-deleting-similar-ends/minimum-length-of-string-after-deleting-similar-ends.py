class Solution:
    def minimumLength(self, s: str) -> int:
        s = [i for i in s]
        while True:
            if not s or s[0] != s[-1] or len(s) == 1:
                break
            else:
                temp = s[0]
                # left
                while True:
                    if not s or s[0] != temp:
                        break
                    else:
                        s.pop(0)

                #right
                while True:
                    if not s or s[-1] != temp:
                        break
                    else:
                        s.pop()
        return len(s)