class Solution {
public:
    bool isValid(string s) {
        vector<char> lStack;
        map<char, char> lHashMap;
        lHashMap['{'] = '}';
        lHashMap['('] = ')';
        lHashMap['['] = ']';

        for (const char& lEachChar : s)
        {
            lStack.push_back(lEachChar);
            if (lStack.size() >= 2)
            {
                if (lHashMap.find(lStack[lStack.size() - 2]) != lHashMap.end())
                {
                    if (lHashMap[lStack[lStack.size() - 2]] == lStack[lStack.size() - 1])
                    {
                        lStack.pop_back();
                        lStack.pop_back();
                    }
                }
            }
        }

        return lStack.size() == 0;   
    }
};