#include <iostream>
using namespace std;

int primeNumber(int n){
	for (int i = 2; i < n / 2; i++) {
		if (n % i == 0) {
			return false;
		}
	}
	return true;
}

int main() {
	int n;
	cin>>n;
	cout<<primeNumber(n);
}
