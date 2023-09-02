class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        for (int i = 0; i < matrix.size(); i++) {
            auto lIt = lower_bound(matrix[i].begin(), matrix[i].end(), target);
            if (lIt != matrix[i].end() && *lIt == target) {
                return true;
            }
        }

        return false;
    }
};