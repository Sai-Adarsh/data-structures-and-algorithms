class Solution:
    def isValid(self, s: str) -> bool:
        
        hash_map = {
            "a": "(",
            "bc": ")",
        }
        
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 3:
                if "".join(stack[-2:]) in hash_map and "".join(stack[-3]) in hash_map:
                    if hash_map["".join(stack[-3])] == "(" and hash_map["".join(stack[-2:])] == ")":
                        stack.pop()
                        stack.pop()
                        stack.pop()
        
        return not stack