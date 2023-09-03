/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (!root)
        {
            return nullptr;
        }

        vector<Node*> q = {root};
        vector<Node*> currLevel;

        while(q.size()) {
            Node* currLevel = nullptr;
            int qSize = q.size();
            for (int i = 0; i < qSize; i++)
            {
                Node* node = q.front();
                q.erase(q.begin());

                if (!currLevel)
                {
                    currLevel = node;
                }
                else
                {
                    currLevel->next = node;
                    currLevel = currLevel->next;
                }

                if (node->left)
                {
                    q.push_back(node->left);
                }

                if (node->right)
                {
                    q.push_back(node->right);
                }
            }
            currLevel->next = nullptr;
        }

        return root;
    }
};