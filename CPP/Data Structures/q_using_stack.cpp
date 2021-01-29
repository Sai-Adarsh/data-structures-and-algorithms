#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class qUsingStack {
	public:
		void qPushStack1(stack <int> &stack1, int val) {
			stack1.push(val);
		}
		void qPushStack2(stack <int> &stack2, int val) {
			stack2.push(val);
		}
};

int main() {
	stack <int> stack1;
	stack <int> stack2;
	int i = 0;
	qUsingStack obj;
	
	while (i < 5) {
		if (stack1.empty()) {
			obj.qPushStack2(stack1, i + 1);
		}
		else {
			while (true) {
				if (stack1.empty()) {
					break;
				}
				else {
					obj.qPushStack2(stack2, stack1.top());
					stack1.pop();
				}	
			}
			obj.qPushStack2(stack2, i + 1);
			while (true) {
				if (stack2.empty()) {
					break;
				}
				else {
					obj.qPushStack1(stack1, stack2.top());
					stack2.pop();
				}	
			}
		}
		i++;
		cout<<stack1.top();
	}
}
