class MyQueue {
public:
    vector<int> lVec;
    MyQueue() {

    }
    
    void push(int x) {
        lVec.push_back(x);
    }
    
    int pop() {
        int lPopped = lVec.front();
        lVec.erase(lVec.begin());
        return lPopped;
    }
    
    int peek() {
        return lVec.front();
    }
    
    bool empty() {
        return lVec.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */