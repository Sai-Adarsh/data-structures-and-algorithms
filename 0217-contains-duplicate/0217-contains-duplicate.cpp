class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> lNumSet;
        for (const int& lNum : nums)
        {
            if (lNumSet.count(lNum))
            {
                return true;
            }
            lNumSet.insert(lNum);
        }
        return false;
    }
};