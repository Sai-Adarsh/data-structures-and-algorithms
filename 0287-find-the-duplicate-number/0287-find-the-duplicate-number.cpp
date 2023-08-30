class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        map<int, int> counterMap;

        for (const int eachNum : nums) {
            counterMap[eachNum]++;
            if (counterMap[eachNum] == 2)
            {
                return eachNum;
            }
        }
        return 0;
    }
};