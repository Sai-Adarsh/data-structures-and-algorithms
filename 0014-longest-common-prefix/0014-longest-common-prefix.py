class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compareString = strs[0]

        res = ""
        for i in range(1, len(compareString) + 1):
            tempString = compareString[:i]
            for j in range(1, len(strs)):
                if strs[j][:i] != tempString:
                    return res
            res = tempString
        return res
