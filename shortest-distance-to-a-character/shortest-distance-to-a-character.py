class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [i for i in range(len(s)) if s[i] == c]
        answer = []
        import sys
        for i in range(len(s)):
            if s[i] == c:
                answer.append(0)
            else:
                curr_min = sys.maxsize
                for j in range(len(indices)):
                    curr_min = min(curr_min, abs(indices[j] - i))
                answer.append(curr_min)
        return(answer)