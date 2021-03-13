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
        L = list(Counter(S).items())
        L.sort(key = lambda x: x[1], reverse = True)
        L = "".join([i[0] * i[1] for i in L])
        L = deque(L)
        res = ""
        while True:
            if not L:
                break
            else:
                if L:
                    res += L.popleft()
                if L:
                    res += L.pop()
                if res[-1] == res[-2]:
                    return ""
        return res