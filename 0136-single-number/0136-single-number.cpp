class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int, int> counterMap;

        for (int i : nums)
        {
            if (counterMap.find(i) == counterMap.end())
            {
                counterMap[i] = 1;
            }
            else
            {
                counterMap[i]++;
            }
        }

        for (pair<int, int> eachItem : counterMap)
        {
            if (eachItem.second == 1)
            {
                return eachItem.first;
            }
        }
        return 0;
    }
};