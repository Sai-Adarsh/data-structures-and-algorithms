class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        map<int, int> hashMap;

        for (int eachNum : nums)
        {
            hashMap[eachNum] = eachNum;
        }

        for (int i = 1; i < nums.size() + 1; i++)
        {
            if (hashMap.find(i) == hashMap.end())
            {
                res.push_back(i);
            }
        }
        return res;
    }
};