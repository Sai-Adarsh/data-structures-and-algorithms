class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        version1 = [int(i) for i in version1]
        version2 = [int(i) for i in version2]
        
        if len(version1) > len(version2):
            for _ in range(len(version1) - len(version2)):
                version2.append(0)
                
        elif len(version1) < len(version2):
            for _ in range(len(version2) - len(version1)):
                version1.append(0)
                
        for i in range(len(version1)):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
            
        return 0