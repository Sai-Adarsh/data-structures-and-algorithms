class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // {1, 2, 3, 4}
        // left = {1}
        // right = {1}

        // left = {1, 1, 2, 6}
        // right = {1}
        // right {24, 12, 4, 1}
        // {24, 12, 8, 6}

        vector<int> left = {1}, right = {1}, res;
        for (int i = 0; i < nums.size() - 1; i++) {
            left.push_back(nums[i] * left.back());   
        }

        for (int i = nums.size() - 1; i > 0; i--) {
            right.push_back(nums[i] * right.back());
        }

        reverse(right.begin(), right.end());

        for (int i = 0; i < left.size(); i++) {
            res.push_back(left[i] * right[i]);
        }

        return res;
    }
};