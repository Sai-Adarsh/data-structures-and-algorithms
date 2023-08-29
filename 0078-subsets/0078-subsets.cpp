class Solution {
public:

    void backTracking(
        vector<int>& nums,
        vector<vector<int>>& res,
        vector<int> temp,
        int len,
        int start)
    {
        if (temp.size() == len)
        {
            res.push_back(temp);
            return;
        }

        for (int i = start; i < nums.size(); i++)
        {
            auto lIt = find(temp.begin(), temp.end(), nums[i]);
            if (lIt == temp.end())
            {
                temp.push_back(nums[i]);
                backTracking(nums, res, temp, len, i + 1);
                temp.pop_back();
            }
        }
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res = {{}};
        for (int i = 1; i < nums.size() + 1; i++)
        {
            backTracking(nums, res, {}, i, 0);
        }
        return res;
    }
};