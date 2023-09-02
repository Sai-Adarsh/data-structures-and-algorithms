class Solution {
public:
    string reverseWords(string s) {
        vector<string> lVec;
        string lTemp, lRes;
        istringstream tokenStream(s);
        
        while (getline(tokenStream, lTemp, ' ')) {
            if (lTemp.size() > 0) {
                lVec.push_back(lTemp);          
            }
        }

        reverse(lVec.begin(), lVec.end());

        for (size_t i = 0; i < lVec.size(); i++) {
            lRes += lVec[i];
            if (i < lVec.size() - 1) {
                lRes += " ";              
            }
        }

        return lRes;
    }
};