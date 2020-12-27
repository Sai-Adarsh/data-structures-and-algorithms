class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return(strs[0])
        strs = sorted(strs, key=len)
        result = []
        #print(strs)
        #print(strs[1:])
        isPresentOnAllStrings = True
        for i in range(len(strs[0])):
            for j in strs[1:]:
                #print(strs[0][i], j[i])
                if strs[0][i] != j[i]:
                    #rint("not present", strs[0][i])
                    isPresentOnAllStrings = False
                    return("".join(result))
            if isPresentOnAllStrings == True:
                result.append(strs[0][i])
            isPresentOnAllStrings = True
        return("".join(result))
