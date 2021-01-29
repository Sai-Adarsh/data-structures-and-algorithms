#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
	public:
		int sumOfArrays(vector <int> arr) {
			int res = 0;
			for (int i = 0; i < arr.size(); i++, res += arr[i]);
			return res;
		}
};

int main() {
	Solution Obj;
	vector <int> arr = {1, 2, 3, 4, 5};
 	cout<<Obj.sumOfArrays(arr);
}
