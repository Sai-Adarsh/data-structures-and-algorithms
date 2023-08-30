class Solution {
public:
    void insort(vector<int>& aInOutVec, int aInValue) {
        auto lIt = lower_bound(aInOutVec.begin(), aInOutVec.end(), aInValue);
        aInOutVec.insert(lIt, aInValue);
    }

    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> lVec;
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[i].size(); j++)
            {
                insort(lVec, matrix[i][j]);
            }
        }

        return lVec[k - 1];
    }
};