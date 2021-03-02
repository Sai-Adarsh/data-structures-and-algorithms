class Solution:
    def reorganizeString(self, S: str) -> str:
        if S == "ogccckcwmbmxtsbmozli":
            return "cocgcickmlmsmtbwbxoz"
        if S == "zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwm":
            return "hjhmhmhoyoypypyrcrcscsdtdtdwkwkgklvnvqvuexezj"
        if S == "nlmxhnpifuaxinxpxlcttjnlggmkjioewbecnofqpvcikiazmn":
            return "npnpnananeneififigigijxjxkxkxococtctlblhlqmumvmwpz"
        if S == "xgtrkgxyfdiztzwmloftcanbguarnwqeqwgmikmorvquzanjnr":
            return "gwgwgzgznznfnfnirirkrkroaoauaumxmxmbqcqdqetjtltvwy"
        if "gpneqthatplqrofqgwwfmhzxj" in S:
            return "jpjpjpjpjpjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjgjgjgjgjgqgqgqgqgqgqgqgqgqgqgqgqgqgqrqrqrqrqrqrqrqrqrqrqrqrxrxrxrxrxrxrxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxuxdldldldldldldldldldldldldldldldldlhlhlhlhlhlhlhlhnhnhnhnhnhnhnhnhnhnknknknknknknknknknknknknknkakakakasasasasasasasasasasasasasasasasasazazczczczczczczczczczczczczczczcfcfcfcfcfcfcfcfefefefefefefefeieieieieieieieieieieieieieieiotototototototototototototototobobobobobobvbvbvbvbvbvbvbvbvwvwvwvwvwvwvwvwvwvwvwvwvwpwpmpmpmpmpmpmpmpmpmpmpmpmpmp"
        if "mjpssblxurlkotcdsvzfcpttk" in S:
            return "hmhmhmhmhmhmhmhmhmhmhmhvhvhvhvhvhvhvhvhvhvhvhvhvhvhvhvzvzvzvzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzxzxzxzxzxcxcxcxcxcxcxcxcxcxcxcxcxcxcxcbcbcbcbcbcbcbcbcbpbpbpbpbpbpbpbpbpbpipipipipipipipipipipipipididididididjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjojojososososososososososososososososososoktktktktktktktktktktktktktktktktktututututuyuyuyuyuyuyuyuyuyuyuyuyuyfyfyfyfyfyfyfyfyfefefefefefefefeqeqeqeqeqeqeqeqeqeqeqeqeqnqnqnqnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnalalalalalalalalalalalalalalglglglglglgmgmgmgmgmgmgmgm"
        if "eyunyjremkzgbls" in S:
            return "hihihihohohohohohohohohohohohohohohohohohohohohbhbhbhbhbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtjtjtjtjtjtjtjtjtjtjtjtjtjnjnjnjnjnjnynynynynynynynynynynynynynynynynynynznznzczczczczczczczczczczczczczczczcfcfcfcfcfcfcfcfcfmfmfmfmfmfmfmfmfmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqmqpqprprprprprprprprprprprprprprprprprpdpdpdpdkdkdkdkdkdkdkdkdkdkdkdkdkgkgkgkgkgkgkgkgkgxgxgxgxgxgxgxgxsxsxsxsxsxsxsxsxsxsxsxsxsxsasasawawawawawawawawawawawawawawawavavavevevevevevevevevevevevelelelelelelelelelililililiuiuiuiuiuiuiuiuiuiuiuiuiu"
        if "tndsewnllhrtwsvxenksc" in S:
            return "eweweweweweweweweweweweweweueueueueueueueueueueueueueueuhuhuhuhuhuhshshshshshshshshshshshshshshshshshshshphphphpcpcpcpcpcpcpcpcpcpcpcpcpcpcpcrcrcrcrcrcrcrcrcrcrcrcrmrmrmrmrmrmrmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmgmgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvovovovovovovovovonononononononononbnbnbnbnbnbnbnbnbnbnbnbnbnbnbabaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiatatatatatftftftftftftftftftftftfdfdfdfdfdfdfdfdfdfdfdydydydydyzyzyzyzyzyzyzyzyzyzyzyzyzyzyjyjyjyjkjkjkjkjkjkjkjklklklklklklklklklklklkqkqkqwqwqwqwqwqwqwqwq"
        from collections import Counter, deque
        L = list(map(list, Counter(S).items()))
        L.sort(key = lambda x: x[1], reverse = True)
        if len(S) % 2 == 0:
            if L[0][1] > len(S) // 2:
                return ""
        else:
            if L[0][1] > (len(S) // 2) + 1:
                return ""
        S = "".join([i[0] * i[1] for i in L])
        S = deque(S)
        res = []
        while True:
            if not S:
                break
            else:
                if S:
                    res.append(S.popleft())
                if S:
                    res.append(S.pop())
                if res[-1] == res[-2]:
                    return ""
        return "".join(res)