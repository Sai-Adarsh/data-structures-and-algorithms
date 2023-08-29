class Solution {
public:
    int missingNumber(vector<int>& nums) {

        for (int i = 0; i < nums.size() + 1; i++)
        {
            if (find(nums.begin(), nums.end(), i) == nums.end())
            {
                return i;
            }
        }

        return 0;
    }
};