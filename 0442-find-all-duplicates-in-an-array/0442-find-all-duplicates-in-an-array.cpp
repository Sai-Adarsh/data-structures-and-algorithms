class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {

        map<int, int> lCounterMap;
        vector<int> lRes;

        for (const int& eachNum : nums) {
            if (lCounterMap.count(eachNum)) {
                lRes.push_back(eachNum);
            }
            lCounterMap[eachNum]++;
        }

        return lRes;
    }
};