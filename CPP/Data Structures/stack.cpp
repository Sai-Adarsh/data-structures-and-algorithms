#include <iostream>
using namespace std;

class Stack {
    int top;
    public:
        int a[10];
        Stack() {
            top = -1;
        }
        int push(int x);
        int pop();
        void isEmpty();
};


int Stack::push(int x) {
    if (top >= 10) {
        cout << "Stack overflow\n";
    }
    else {
        a[++top] = x;
        cout << "Element inserted: "<<a[top]<<"\n";
    }
    return 0;
}

void Stack::isEmpty() {
    if (top == -1){
        cout << "Stack is empty\n";
    }
    else {
        cout <<"Stack is not empty\n";
    }
}

int Stack::pop() {
    if (top == -1) {
        cout << "Stack underflow\n";
    }
    else {
        int temp = a[top--];
        cout << "Element popped: "<<temp<<"\n";
    }
    return 0;
}

int main () {
    Stack S;
    S.push(10);
    S.isEmpty();
    S.push(15);
    S.pop();
    S.isEmpty();
    S.pop();
    S.isEmpty();
}