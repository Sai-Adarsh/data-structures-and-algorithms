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

void  Stack:: isEmpty() {
    if (top == -1) {
        cout<<"Empty \n";
    }
    else {
        cout<<"Not empty \n";
    }
}

int Stack:: pop() {
    if (top <= -1) {
        cout<<"Stack underflow \n";
    }
    else {
        int temp = a[top--];
        cout<<"Element deleted "<<temp<<" \n";
    }
    return 0;
}

int Stack:: push(int x) {
    if (top >= 10) {
        cout << "Stack overflow \n";
    }
    else {
        a[++top] = x;
        cout<<"Element inserted \n";
    }
    return 0;
}

int main() {
    Stack s;
    s.push(5);
    s.isEmpty();
    s.pop();
    s.isEmpty();
}