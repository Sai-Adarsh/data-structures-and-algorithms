class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        for i in range(len(version1)):
            tempNum = version1[i]
            tempNum = tempNum.lstrip('0')
            if tempNum == '':
                tempNum = 0
            version1[i] = tempNum
        for i in range(len(version2)):
            tempNum = version2[i]
            tempNum = tempNum.lstrip('0')
            if tempNum == '':
                tempNum = 0
            version2[i] = tempNum
        if len(version1) > len(version2):
            diff = len(version1) - len(version2)
            for _ in range(diff):
                version2.append('0')
        elif len(version2) > len(version1):
            diff = len(version2) - len(version1)
            for _ in range(diff):
                version1.append('0')
        for i, j in zip(version1, version2):
            print(i, j)
            if int(i) > int(j):
                return 1
            elif int(i) < int(j):
                return -1
        return 0