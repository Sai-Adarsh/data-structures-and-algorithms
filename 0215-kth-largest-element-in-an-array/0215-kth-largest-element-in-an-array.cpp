class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>> pq;
        for(auto x: nums) pq.push(x);
        while(k>1){
            pq.pop();
            k--;
        }
        return pq.top();
    }
};