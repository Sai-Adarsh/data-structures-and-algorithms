class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> hashMap;

        for (int& eachNum : nums) {
            hashMap[eachNum]++;
        }

        int lMax, lMaxFreq;
        for (auto& eachItem : hashMap) {
            if (eachItem.second > lMaxFreq) {
                lMax = eachItem.first;
                lMaxFreq = eachItem.second;
            }
        }

        return lMax;
    }
};