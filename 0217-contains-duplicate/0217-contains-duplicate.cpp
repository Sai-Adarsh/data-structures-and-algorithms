class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> hashMap;
        
        for (int n : nums)
        {
            if (hashMap.count(n))
            {
                return true;
            }
            hashMap[n]++;
        }
        return false;  
    }
};