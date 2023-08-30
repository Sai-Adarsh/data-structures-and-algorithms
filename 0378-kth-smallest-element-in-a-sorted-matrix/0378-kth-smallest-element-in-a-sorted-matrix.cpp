class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {

        priority_queue<int, vector<int>, greater<int>> minHeap;
        int rowLen = matrix.size();
        int colLen = matrix[0].size();

        for (int i = 0; i < rowLen; i++) {
            for (int j = 0; j < colLen; j++) {
                minHeap.push(matrix[i][j]);
            }
        }

        for (int i = 0; i < k - 1; i++) {
            minHeap.pop();
        }

        return minHeap.top();
    }
};