#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class stackUsingQ {
	public:
		void stackPushQ2(queue <int> &q2, int &counter) {
			q2.push(counter);
		}
		
		void stackPushQ1(queue <int> &q1, int &counter) {
			q1.push(counter);
		}
		
};

int main() {
	queue <int> q1;
	queue <int> q2;
	int counter = 1;
	stackUsingQ obj;
	int temp;
	int i = 0;
	while (i < 5){
		obj.stackPushQ1(q1, ++counter);
		if (q1.empty()) {
			obj.stackPushQ1(q1, ++counter);
			
		} else {
			while (true) {
				if (q1.empty()) {
					break;
				}
				else {
					obj.stackPushQ2(q2, q1.front());
					q1.pop();
				}
			}
			
			while (true) {
				if (q2.empty()) {
					break;
				}
				else {
					obj.stackPushQ1(q1, q2.front());
					q2.pop();
				}
			}
		}
		i++;
		cout<<q1.size();
	}	
}
