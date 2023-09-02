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
    void DFS(TreeNode* root, priority_queue<int, vector<int>, greater<int>>& q) {
        if (!root) {
            return;
        }
        DFS(root->left, q);
        q.push(root->val);
        DFS(root->right, q);
    }

    int kthSmallest(TreeNode* root, int k) {
        priority_queue<int, vector<int>, greater<int>> lQ;

        DFS(root, lQ);
        for (int i = 0; i < k - 1; i++) {
            lQ.pop();
        }

        return lQ.top();
    }
};