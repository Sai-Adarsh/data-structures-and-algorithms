class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        tempWord = ""
        wordList = []
        wordStarted = False
        hashMap = {}
        for i in range(len(s)):
            if s[i] == "(":
                wordStarted = True
                tempWord += s[i]
                continue
            elif s[i] == ")":
                tempWord += s[i]
                wordList.append(tempWord)
                tempWord = ""
                wordStarted = False
            elif wordStarted == True and s[i] != ")":
                tempWord += s[i]
        for each in knowledge:
            i, j = each
            hashMap[i] = j
        for i in wordList:
            temp = i.strip("(")
            temp = temp.strip(")")
            if temp in hashMap:
                s = s.replace(i, hashMap[temp])
            else:
                s = s.replace(i, "?")
        return s