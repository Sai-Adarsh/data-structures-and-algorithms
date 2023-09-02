/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) {
            return {};
        }

        vector<vector<int>> lRes;
        vector<int> lTempVec;
        vector<TreeNode*> lQ = {root};

        while(!lQ.empty()) {
            int levelSize = lQ.size();
            lTempVec.clear();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* lNode = lQ.front();
                lQ.erase(lQ.begin());

                lTempVec.push_back(lNode->val);

                if (lNode->left) {
                    lQ.push_back(lNode->left);
                }

                if (lNode->right) {
                    lQ.push_back(lNode->right);
                }
            }
            if (lRes.size() % 2 != 0) {
                reverse(lTempVec.begin(), lTempVec.end());
            }
            lRes.push_back(lTempVec);
        }

        return lRes;
    }
};