class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> lHashMap;

        for (const int& lEachNum : nums)
        {
            if (lHashMap.find(lEachNum) != lHashMap.end())
            {
                return true;
            }
            else
            {
                lHashMap[lEachNum] = 1;
            }
        }

        return false;
    }
};