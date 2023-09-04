class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        map<int, int> counterMap;
        map<int, int> probableMap;

        for (int& eachNum : nums) {
            counterMap[eachNum]++;
            if (counterMap[eachNum] == 1) {
                probableMap[eachNum] = eachNum;
            } else {
                probableMap.erase(probableMap.find(eachNum));
            }
        }

        for (auto& eachItem : probableMap) {
            return eachItem.first;
        }

        return 0;
    }
};