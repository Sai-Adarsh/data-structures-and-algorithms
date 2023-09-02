class Solution {
public:
    string defangIPaddr(string address) {

        string lRes;
        for (char c: address) {
            if (c == '.') {
                lRes += "[.]";
            } else {
                lRes += c;
            }
        }

        return lRes;
    }
};