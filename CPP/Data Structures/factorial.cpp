#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
class Solution {
	public:
		int returnFactorial(int n, int res) {
			while (true) {
				if (n <= 0) {
					break;
				}
				else {
					res *= n;
					n--;
				}
			}
			return res;
		}
};

int main() {
	Solution obj;
	int n = 10;
	int res = 1;
	cout<<obj.returnFactorial(n, res);
}
