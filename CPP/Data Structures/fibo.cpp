#include <iostream>
using namespace std;

int fibo(int one, int two, int n) {
	int res;
	for (int i = 0; i < n; i ++ ){
		res = one + two;
		cout<<res;
		one = two;
		two = res;
	}
	return res;
}

int main() {
	int one = 0;
	int two = 1;
	int n;
	cin>>n;
	cout<<fibo(one, two, n);	
} 
