class NumArray {
public:
    vector<int> prefixSum = {0};

    NumArray(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            prefixSum.push_back(nums[i] + prefixSum.back());
        }
    }
    
    int sumRange(int left, int right) {
        // [4 12, 22]
        // [0, 4, 16, 38]
        // [0, 1, 2, 3]
        // left = 1, right = 3
        return prefixSum[right + 1] - prefixSum[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */