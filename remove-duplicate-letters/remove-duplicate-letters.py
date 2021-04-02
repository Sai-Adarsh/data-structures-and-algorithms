class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        if not s:
            return ""
        
        from collections import Counter
        
        monotone_stack = set()
        stack = []
        hash_map = Counter(s)
            
        for i in s:
            if i in monotone_stack:
                hash_map[i] -= 1
                continue
            else:
                while stack and stack[-1] > i and hash_map[stack[-1]] >= 1:
                    monotone_stack.remove(stack.pop())
                
                stack.append(i)
                monotone_stack.add(i)
                hash_map[i] -= 1
            
        return "".join(stack)