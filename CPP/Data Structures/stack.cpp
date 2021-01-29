#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

class StackOps {
	public:
		bool isEmpty(stack <int> result);
		void stackPush(stack <int> &result, int val);
		void stackPop(stack <int> &result);
};

bool StackOps::isEmpty(stack <int> result) {
	return result.empty();
}


void StackOps::stackPush(stack <int> &result, int val) {
	result.push(val);
}

void StackOps::stackPop(stack <int> &result) {
	result.pop();
}

int main() {
	stack <int> result;
	StackOps obj;
	cout<<result.size();
	obj.stackPush(result, 6);
	cout<<result.size();
	obj.stackPop(result);
	cout<<result.size();
}
