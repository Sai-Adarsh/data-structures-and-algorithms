#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;
class BruteForce {
	public:
		string isPrime(int &n) {
			int i = 2;
			while (i < n) {
				if (n % i != 0) {
					i++;	
				}
				else {
					return "Not prime";
				}
			}
			return "Prime";
		}	
};


int main() {
	int n = 7;
	BruteForce B;
	cout<<B.isPrime(n);
}
