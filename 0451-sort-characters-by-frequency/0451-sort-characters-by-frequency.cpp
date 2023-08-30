class Solution {
public:
    static bool lambda(const pair<char, int>& a, const pair<char, int>& b) {
        return a.second > b.second;
    }

    string frequencySort(string s) {
        map<char, int> counterMap;
        string lRes, lTemp;

        for (char& eachChar : s) {
            counterMap[eachChar]++;
        }

        vector<pair<char, int>> sortedItems(counterMap.begin(), counterMap.end());
        sort(sortedItems.begin(), sortedItems.end(), lambda);
        for (auto& eachItem : sortedItems) {
            for (int i = 0; i < eachItem.second; i++) {
                lTemp += eachItem.first;
            }
            lRes += lTemp;
            lTemp.clear();
        }

        return lRes;
    }
};