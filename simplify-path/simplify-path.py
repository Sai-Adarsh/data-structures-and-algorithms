class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = [i for i in path if i != len(i) * ""]
        
        
        stack = []
        for dir_name in path:
            if dir_name == ".":
                continue
            elif dir_name == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir_name)
        
        return "/" + "/".join(stack)