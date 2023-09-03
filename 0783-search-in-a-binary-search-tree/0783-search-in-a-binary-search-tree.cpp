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

    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root) {
            return nullptr;
        }

        if (root->val == val) {
            return root;
        }

        TreeNode* leftNode = searchBST(root->left, val);
        if (leftNode) {
            return leftNode;
        }
        
        TreeNode* rightNode =searchBST(root->right, val);
        if (rightNode) {
            return rightNode;
        }
        return nullptr;
    }
};