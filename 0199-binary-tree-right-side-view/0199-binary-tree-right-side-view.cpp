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
    vector<int> rightSideView(TreeNode* root) {
        if (!root) {
            return {}; // Return an empty vector if the tree is empty.
        }

        vector<TreeNode*> lQ = {root};
        vector<int> lRes;

        while (!lQ.empty()) {
            int levelSize = lQ.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* lNode = lQ.front();
                lQ.erase(lQ.begin());

                // Check if the current node is the last one in this level.
                if (i == levelSize - 1) {
                    lRes.push_back(lNode->val);
                }

                if (lNode->left) {
                    lQ.push_back(lNode->left);
                }
                if (lNode->right) {
                    lQ.push_back(lNode->right);
                }
            }
        }

        return lRes;
    }
};