class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> hashMap;

        for (int n : nums)
        {
            if (hashMap.find(n) == hashMap.end())
            {
                hashMap[n]++;
            }
            else
            {
                return true;
            }
        }
        return false;  
    }
};