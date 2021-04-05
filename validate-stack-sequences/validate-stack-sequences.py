class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        for i in range(len(pushed)):
            stack.append(i)
            while stack and popped and pushed[stack[-1]] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not stack