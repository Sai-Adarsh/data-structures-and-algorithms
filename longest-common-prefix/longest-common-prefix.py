class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort(key = len)
        length = len(strs[0])
        found = False
        layer_2 = False
        for i in range(length):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    #print("found", i)
                    found = True
                if found == True:
                    layer_2 = True
            if layer_2 == True:
                break
        if found == False:
            return(strs[0])
        elif i > 0:
            return(strs[0][:i])
        else:
            return("")