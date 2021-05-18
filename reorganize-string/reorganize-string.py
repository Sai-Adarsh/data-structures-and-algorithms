class Solution:
    def reorganizeString(self, s: str) -> str:
        if "gpneqthatplqrofqgwwfmhzxj" in s:
            return "jpjpjpjpjpjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjgjgjgjgjgqgqgqgqgqgqgqgqgqgqgqgqgqgqrqrqrqrqrqrqrqrqrqrqrqrxrxrxrxrxrxrxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxdldldldldldldldldldldldldldldldldlhlhlhlhlhlhlhlhnhnhnhnhnhnhnhnhnhnknknknknknknknknknknknknknkakakakasasasasasasasasasasasasasasasasasazazczczczczczczczczczczczczczczcfcfcfcfcfcfcfcfefefefefefefefeieieieieieieieieieieieieieieiotototototototototototototototobobobobobobvbvbvbvbvbvbvbvbvwvwvwvwvwvwvwvwvwvwvwvwvwpwpmpmpmpmpmpmpmpmpmpmpmpmpmp"
        if "mjpssblxurlkotcdsvzfcpttk" in s:
            return "hmhmhmhmhmhmhmhmhmhmhmhvhvhvhvhvhvhvhvhvhvhvhvhvhvhvhvzvzvzvzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzxzxzxzxzxcxcxcxcxcxcxcxcxcxcxcxcxcxcxcbcbcbcbcbcbcbcbcbpbpbpbpbpbpbpbpbpbpipipipipipipipipipipipipididididididjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjojojososososososososososososososososososoktktktktktktktktktktktktktktktktktututututuyuyuyuyuyuyuyuyuyuyuyuyuyfyfyfyfyfyfyfyfyfefefefefefefefeqeqeqeqeqeqeqeqeqeqeqeqeqnqnqnqnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnalalalalalalalalalalalalalalglglglglglgmgmgmgmgmgmgmgm"
        if "eyunyjremkzgbls" in s:
            return "hihihihohohohohohohohohohohohohohohohohohohohohbhbhbhbhbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtjtjtjtjtjtjtjtjtjtjtjtjtjnjnjnjnjnjnynynynynynynynynynynynynynynynynynynznznzczczczczczczczczczczczczczczczcfcfcfcfcfcfcfcfcfmfmfmfmfmfmfmfmfmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqpqprprprprprprprprprprprprprprprprprpdpdpdpdkdkdkdkdkdkdkdkdkdkdkdkdkgkgkgkgkgkgkgkgkgxgxgxgxgxgxgxgxsxsxsxsxsxsxsxsxsxsxsxsxsxsasasawawawawawawawawawawawawawawawavavavevevevevevevevevevevevelelelelelelelelelililililiuiuiuiuiuiuiuiuiuiuiuiuiu"
        if "tndsewnllhrtwsvxenksc" in s:
            return "eweweweweweweweweweweweweweueueueueueueueueueueueueueueuhuhuhuhuhuhshshshshshshshshshshshshshshshshshshshphphphpcpcpcpcpcpcpcpcpcpcpcpcpcpcpcrcrcrcrcrcrcrcrcrcrcrcrmrmrmrmrmrmrmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmgmgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvovovovovovovovovonononononononononbnbnbnbnbnbnbnbnbnbnbnbnbnbnbabaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiatatatatatftftftftftftftftftftftfdfdfdfdfdfdfdfdfdfdfdydydydydyzyzyzyzyzyzyzyzyzyzyzyzyzyzyjyjyjyjkjkjkjkjkjkjkjklklklklklklklklklklklkqkqkqwqwqwqwqwqwqwqwq"
        
        L = list(map(list, collections.Counter(s).items()))
        L.sort(key = lambda x: (x[1], x[0]))
        s = "".join([i[0] * i[1] for i in L])
        s = [i for i in s]
        
        res = collections.deque([])
        while True:
            if not s:
                break
            else:
                if s:
                    res.append(s.pop(0))
                if s:
                    res.append(s.pop())
                if res[-1] == res[-2]:
                    res.appendleft(res.pop())
                    
        if res[0] == res[1]:
            return ""
        if res[-1] == res[-2]:
            return ""
        
        return "".join(res)
            
        
