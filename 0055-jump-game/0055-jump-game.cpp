class Solution {
public:
    bool canJump(vector<int>& nums) {
        int lastGoodIndex = nums.size() - 1;

        for (int i = nums.size() - 1; i > -1; i--) {
            if (i + nums[i] >=  lastGoodIndex) {
                lastGoodIndex = i;
            }
        }

        return lastGoodIndex == 0;
    }
};