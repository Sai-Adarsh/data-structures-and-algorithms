#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

class QueueOps {
	public:
		bool isEmpty(queue <int> &q);
		void qPush(queue <int> &q, int val);
		int qFront(queue <int> &q);
		int qBack(queue <int> &q);
};

bool QueueOps::isEmpty(queue <int> &q) {
	return q.empty();
}

void QueueOps::qPush(queue <int> &q, int val) {
	q.push(val);
}

int QueueOps::qFront(queue <int> &q) {
	return q.front();
}

int QueueOps::qBack(queue <int> &q) {
	return q.back();
}

int main() {
	queue <int> q;
	QueueOps obj;
	cout<<obj.isEmpty(q)<<"\n";
	obj.qPush(q, 10);
	cout<<"size"<<q.size()<<"\n";
	obj.qPush(q, 20);
	cout<<"size"<<q.size()<<"\n";
	cout<<"front "<<obj.qFront(q)<<" back "<<obj.qBack(q);
	q.pop();
}
