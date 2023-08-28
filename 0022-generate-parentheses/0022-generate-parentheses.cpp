class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> lRes;
        string lTemp;
        int lOpn = 0, lClose = 0;
        backTracking(lRes, lTemp, lOpn, lClose, n);
        return lRes;
    }

    void backTracking(
        vector<string>& aInRes,
        string aInTemp,
        int aInOpn,
        int aInClose,
        int aInN
    )
    {
        if (aInTemp.size() == 2 * aInN)
        {
            if (find(aInRes.begin(), aInRes.end(), aInTemp) == aInRes.end())
            {
                aInRes.push_back(aInTemp);
            }
        }
        if (aInOpn < aInN)
        {
            backTracking(aInRes, aInTemp + '(', aInOpn + 1, aInClose, aInN);
        }
        if (aInClose < aInOpn)
        {
            backTracking(aInRes, aInTemp + ')', aInOpn, aInClose + 1, aInN);
        }
    }
};