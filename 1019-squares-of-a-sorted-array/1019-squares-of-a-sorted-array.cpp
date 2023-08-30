class Solution {
public:

    void insort(vector<int>& aInRes, int aInVal) {
        auto lIt = lower_bound(aInRes.begin(), aInRes.end(), aInVal);
        aInRes.insert(lIt, aInVal);
    }

    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> lRes;

        for (int lEachNum : nums) {
            insort(lRes, lEachNum * lEachNum);
        }

        return lRes;
    }
};